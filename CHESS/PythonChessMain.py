#! /usr/bin/env python
"""
 Project: Python Chess
 File name: PythonChessMain.py
 Description:"""

from ChessBoard import ChessBoard
from ChessAI import ChessAI_random, ChessAI_defense, ChessAI_offense
from ChessPlayer import ChessPlayer
from ChessGUI_text import ChessGUI_text
from ChessGUI_pygame import ChessGUI_pygame
from ChessRules import ChessRules
from ChessGameParams import TkinterGameSetupParams
from jake import jake
from victoria import victoria
from derrota import derrota
from empate import empate
from confirmarDerrota import confirmarDerrota
from tipoConexion import conexion
from optparse import OptionParser
import time
import socket
import pygame
from ventanaServidor import ventanaServer
from ventanaCliente import ventanaClient
import sys
import thread
import select

class PythonChessMain:

	def __init__(self,options):
		if options.debug:
			self.Board = ChessBoard(2)
			self.debugMode = True
		else:
			self.Board = ChessBoard(0)#0 for normal board setup; see ChessBoard class for other options (for testing purposes)
			self.debugMode = False

		self.Rules = ChessRules()

	def SetUp(self,options):
		#gameSetupParams: Player 1 and 2 Name, Color, Human/AI level
		if self.debugMode:
			player1Name = 'Atahualpa'
			player1Type = 'humano'
			player1Color = 'blanco'
			player2Name = 'Huascar'
			player2Type = 'randomAI'
			player2Color = 'negro'
		else:
			GameParams = TkinterGameSetupParams()
			(player1Name, player1Color, player1Type, player2Name, player2Color, player2Type) = GameParams.GetGameSetupParams()

		self.player = [0,0]
		self.redis = player1Type
		if player1Type == 'humano':
			self.player[0] = ChessPlayer(player1Name,player1Color)
		elif player1Type == 'server':
			self.player[0] = ChessPlayer(player1Name,player1Color)
		elif player1Type == 'client':
			self.player[0] = ChessPlayer(player2Name,player2Color)
		elif player1Type == 'offenseAI':
			self.player[0] = ChessAI_offense(player1Name,player1Color)

		if player2Type == 'humano':
			self.player[1] = ChessPlayer(player2Name,player2Color)
		elif player2Type == 'server':
			self.player[1] = ChessPlayer(player1Name,player1Color)
		elif player2Type == 'client':
			self.player[1] = ChessPlayer(player2Name,player2Color)
		elif player2Type == 'offenseAI':
			self.player[1] = ChessAI_offense(player2Name,player2Color)


		if options.pauseSeconds > 0:
			self.AIpause = True
			self.AIpauseSeconds = int(options.pauseSeconds)
		else:
			self.AIpause = False

		#create the gui object - didn't do earlier because pygame conflicts with any gui manager (Tkinter, WxPython...)
		if options.text:
			self.guitype = 'text'
			self.Gui = ChessGUI_text()
		else:
			self.guitype = 'pygame'
			if options.old:
				self.Gui = ChessGUI_pygame(0)
			else:
				self.Gui = ChessGUI_pygame(1)

	"""def reDato(self,s,sc):
		print "globales"
		global hilo
		global datito
		print "esperando mensaje"
		mensaje = sc.recv(1024)
		print "recibido"
		datito=mensaje
		print "hilito"
		hilo = 1
        print "brack"""

	def MainLoop(self):
		hilo=0
		datito="123"
		s=0
		sc=0
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		#s.settimeout(20)
		verify = 2
		if self.redis=='server':
			verify=0
			serv=ventanaServer()
			(direccion)=serv.GetipServer()
			if direccion == '0':
				pygame.quit()
				sys.exit(0)
			else :
				s.bind((direccion, 9999))
				s.listen(1)
				s.settimeout(20)
				#s.setblocking (0)
				print "Esperando conexion..."
				sc,adr = s.accept()
				#sc.settimeout(20)
				#sc.setblocking (0)
		elif self.redis=='client':
			verify=1
			clie=ventanaClient()
			(direccion1)=clie.GetipClient()
			if direccion1 == '0':
				pygame.quit()
				sys.exit(0)
			else :
				s.connect((direccion1, 9999))
		currentPlayerIndex = 0
		turnCount = 0
		sinComer = 0
		reySoloBlanco = 0
		reySoloNegro = 0
		reySolo=0
		ayniN = 0
		ayniB = 0
		while not self.Rules.IsCheckmate(self.Board.GetState(),self.player[currentPlayerIndex].color,ayniB,ayniN):
			board = self.Board.GetState()
			currentColor = self.player[currentPlayerIndex].GetColor()
			#hardcoded so that player 1 is always white
			if currentColor == 'blanco':
				turnCount = turnCount + 1
			self.Gui.PrintMessage("")
			baseMsg = "TURNO %s - %s (%s)" % (str(turnCount),self.player[currentPlayerIndex].GetName(),currentColor)
			self.Gui.PrintMessage("-----%s-----" % baseMsg)
			self.Gui.Draw(board)
			if self.Rules.IsInCheck(board,currentColor):
				self.Gui.PrintMessage("Peligro..."+self.player[currentPlayerIndex].GetName()+" ("+self.player[currentPlayerIndex].GetColor()+") esta en jaque")
				jak = jake()
				(ka) = jak.aviso()
			if currentColor== 'negro'and verify ==0 :#self.player[currentPlayerIndex].GetType() == 'server' and turnCount%2!=0: blanco espera movimiento
				"""#s.settimeout(20)
				#s.setblocking (0)
				#hilo=False
				print "ejecutando el treaht"
				thread.start_new_thread(self.reDato,(s,sc))
				hilo=0
				print hilo,"bucle infinito"
				while (hilo==0):
						pass
				#hilo=True
				print "salio de bucle",hilo
				recibido=datito"""
				recibido = sc.recv(1024)
				if recibido=="empate":
						empa=confirmarDerrota()
						(empat)=empa.confirmacionEmpate()
						if empat==1:
							sc.send("aceptar")
							em=empate()
							(emp)=em.mostrarEmpate()
							self.Gui.EndGame(board)
						elif empat==2:
							sc.send("no")
							recibido = sc.recv(1024)
				elif recibido=="salir":
						vi=victoria()
						(vic)=vi.mostrarVictoria()
						self.Gui.EndGame(board)
				else:
						numero=int(recibido)
						Aa=numero/1000
						AA=numero%1000
						Ee=AA/100
						EE=AA%100
						Ii=EE/10
						II=EE%10
						moveTuple=(Aa,Ee),(Ii,II)

			elif currentColor== 'blanco'and verify==0 :#self.player[currentPlayerIndex].GetType() == 'client' and turnCount%2==0: blanco hace su movimiento
				moveTuple = self.Gui.GetPlayerInput(board,currentColor,verify,s,sc,ayniB,ayniN)
				(a,e),(i,o)=moveTuple
				A=str(a)
				E=str(e)
				I=str(i)
				O=str(o)
				mensaje=A+E+I+O
				sc.send(mensaje)
			elif currentColor== 'blanco'and verify==1: #negro espera movimiento
				recibido = s.recv(1024)
				if recibido=="empate":
						empa=confirmarDerrota()
						(empat)=empa.confirmacionEmpate()
						if empat==1:
							s.send("aceptar")
							em=empate()
							(emp)=em.mostrarEmpate()
							self.Gui.EndGame(board)
						elif empat==2:
							s.send("no")
							recibido = s.recv(1024)
				elif recibido=="salir":
						vi=victoria()
						(vic)=vi.mostrarVictoria()
						self.Gui.EndGame(board)
				else:
						numero=int(recibido)
						Aa=numero/1000
						AA=numero%1000
						Ee=AA/100
						EE=AA%100
						Ii=EE/10
						II=EE%10
						moveTuple=(Aa,Ee),(Ii,II)
			elif currentColor== 'negro'and verify==1: #blanco hace su movimiento
				moveTuple = self.Gui.GetPlayerInput(board,currentColor,verify,s,sc,ayniB,ayniN)
				(a,e),(i,o)=moveTuple
				A=str(a)
				E=str(e)
				I=str(i)
				O=str(o)
				mensaje=A+E+I+O
				s.send(mensaje)
			else:
				moveTuple = self.Gui.GetPlayerInput(board,currentColor,verify,s,sc,ayniB,ayniN)
			moveReport,contadorsito,solito,ayni = self.Board.MovePiece(moveTuple) #moveReport = string like "White Bishop moves from A1 to C3" (+) "and captures ___!"
			self.Gui.PrintMessage(moveReport)
			currentPlayerIndex = (currentPlayerIndex+1)%2 #this will cause the currentPlayerIndex to toggle between 1 and 0
			if ayni==1:
				ayniB=ayniB+1
				print ayniB,"y",ayniN
			elif ayni==2:
				ayniN=ayniN+1
				print ayniB,"y",ayniN
			if contadorsito==1:
				sinComer=sinComer+1
			else:
				sinComer=0
			if solito==1:
				reySoloNegro=reySoloNegro+1
			elif solito==0:
				reySoloBlanco=reySoloBlanco+1
			if reySoloBlanco==14 or reySoloNegro==14:
				reySolo=reySolo+1
			if sinComer==28 or reySolo==15:
				em=empate()
				(emp)=em.mostrarEmpate()
				self.Gui.EndGame(board)

		s.close()
		self.Gui.PrintMessage("--------------------------------------------------     JAKE MATE")
		winnerIndex = (currentPlayerIndex+1)%2
		self.Gui.PrintMessage(self.player[winnerIndex].GetName()+" ("+self.player[winnerIndex].GetColor()+") gano el juego")
		if (self.player[winnerIndex].GetColor()=='blanco' and verify==0) or (self.player[winnerIndex].GetColor()=='negro' and verify==1):
			vi = victoria()
			(vic) = vi.mostrarVictoria()
		elif (self.player[winnerIndex].GetColor()=='negro' and verify==0) or (self.player[winnerIndex].GetColor()=='blanco' and verify==1):
			dec = derrota()
			(derr) = dec.mostrarDerrota()
		else:
			vi = victoria()
			(vic) = vi.mostrarVictoria()
		self.Gui.EndGame(board)

parser = OptionParser()
parser.add_option("-d", dest="debug",
				  action="store_true", default=False, help="Enable debug mode (different starting board configuration)")
parser.add_option("-t", dest="text",
				  action="store_true", default=False, help="Use text-based GUI")
parser.add_option("-o", dest="old",
				  action="store_true", default=False, help="Use old graphics in pygame GUI")
parser.add_option("-p", dest="pauseSeconds", metavar="SECONDS",
				  action="store", default=0, help="Sets time to pause between moves in AI vs. AI games (default = 0)")


(options,args) = parser.parse_args()

game = PythonChessMain(options)
game.SetUp(options)
#game.reDato()
game.MainLoop()



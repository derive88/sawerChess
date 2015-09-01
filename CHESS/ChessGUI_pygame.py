#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
 Project: Python Chess
 File name: ChessGUI_pygame.py"""

import pygame
import os
import sys
from pygame.locals import *
from ChessRules import ChessRules
from ScrollingTextBox import ScrollingTextBox
from ChessBoard import ChessBoard
from ChessGameParams1 import TGameSetupParams
from ascenso import Ascenso
from exits import exits
from victoria import victoria
from derrota import derrota
from empate import empate
import socket

class ChessGUI_pygame:
	def __init__(self,graphicStyle=1):
		os.environ['SDL_VIDEO_CENTERED'] = '1' #should center pygame window on the screen
		self.Rules = ChessRules()
		col1 = TGameSetupParams()
		(color_tablero)=col1.GetGameSetupParams()
		self.estilo = color_tablero
		pygame.init()
		pygame.display.init()
		icono=pygame.image.load(os.path.join(r"C:\Program files\Eusebio la doble Marca\M2.1 CHESS\images\icono2.png"))
		pygame.display.set_icon(icono)
		self.screen = pygame.display.set_mode((1075,750))
		self.boardStart_x = 325  #350
		self.boardStart_y = 20
		pygame.display.set_caption('ACHANK´ARA (AJEDREZ AMAUTICO)')

		self.textBox = ScrollingTextBox(self.screen,750,1050,50,650)
		self.LoadImages(graphicStyle)
		#pygame.font.init() - should be already called by pygame.init()
		self.fontDefault = pygame.font.SysFont(r"C:\Program files\Eusebio la doble Marca\M2.1 CHESS\images\arial.ttf", 20 )



	def LoadImages(self, graphicStyle):
		BLANCO = (255, 255, 255)
		VERDE = (0, 255, 0)
		#estilo = "1"

		self.square_size = 50 #all images must be images 50 x 50 pixels
		self.cyan = pygame.image.load(os.path.join(r"C:\Program files\Eusebio la doble Marca\M2.1 CHESS\images\cyan.png")).convert()
		self.cyan.set_colorkey(VERDE)
		self.cyan_square = self.cyan
		self.cyan_square = pygame.transform.rotate(self.cyan, 45)

		self.black_pawn = pygame.image.load(os.path.join(r"C:\Program files\Eusebio la doble Marca\M2.1 CHESS\images\peonnegro2.png")).convert()
		self.black_pawn = pygame.transform.scale(self.black_pawn, (self.square_size,self.square_size))
		self.black_pawn.set_colorkey(VERDE)
		self.black_rook = pygame.image.load(os.path.join(r"C:\Program files\Eusebio la doble Marca\M2.1 CHESS\images\torrenegra2.png")).convert()
		self.black_rook = pygame.transform.scale(self.black_rook, (self.square_size,self.square_size))
		self.black_rook.set_colorkey(VERDE)
		self.black_knight = pygame.image.load(os.path.join(r"C:\Program files\Eusebio la doble Marca\M2.1 CHESS\images\llamanegra2.png")).convert()
		self.black_knight = pygame.transform.scale(self.black_knight, (self.square_size,self.square_size))
		self.black_knight.set_colorkey(VERDE)
		self.black_bishop = pygame.image.load(os.path.join(r"C:\Program files\Eusebio la doble Marca\M2.1 CHESS\images\Chess_tile_bd.png")).convert()
		self.black_bishop = pygame.transform.scale(self.black_bishop, (self.square_size,self.square_size))
		self.black_bishop.set_colorkey(VERDE)
		self.black_king = pygame.image.load(os.path.join(r"C:\Program files\Eusebio la doble Marca\M2.1 CHESS\images\Chess_tile_kd.png")).convert()
		self.black_king = pygame.transform.scale(self.black_king, (self.square_size,self.square_size))
		self.black_king.set_colorkey(VERDE)
		self.black_queen = pygame.image.load(os.path.join(r"C:\Program files\Eusebio la doble Marca\M2.1 CHESS\images\Chess_tile_qd.png")).convert()
		self.black_queen = pygame.transform.scale(self.black_queen, (self.square_size,self.square_size))
		self.black_queen.set_colorkey(VERDE)
		self.black_jilanko = pygame.image.load(os.path.join(r"C:\Program files\Eusebio la doble Marca\M2.1 CHESS\images\jilankonegro2.png")).convert()
		self.black_jilanko = pygame.transform.scale(self.black_jilanko, (self.square_size,self.square_size))
		self.black_jilanko.set_colorkey(VERDE)

		self.white_pawn = pygame.image.load(os.path.join(r"C:\Program files\Eusebio la doble Marca\M2.1 CHESS\images\peonblanco.png")).convert()
		self.white_pawn = pygame.transform.scale(self.white_pawn, (self.square_size,self.square_size))
		self.white_pawn.set_colorkey(VERDE)
		self.white_rook = pygame.image.load(os.path.join(r"C:\Program files\Eusebio la doble Marca\M2.1 CHESS\images\torreblanca.png")).convert()
		self.white_rook = pygame.transform.scale(self.white_rook, (self.square_size,self.square_size))
		self.white_rook.set_colorkey(VERDE)
		self.white_knight = pygame.image.load(os.path.join(r"C:\Program files\Eusebio la doble Marca\M2.1 CHESS\images\llamablanca.png")).convert()
		self.white_knight = pygame.transform.scale(self.white_knight, (self.square_size,self.square_size))
		self.white_knight.set_colorkey(VERDE)
		self.white_bishop = pygame.image.load(os.path.join(r"C:\Program files\Eusebio la doble Marca\M2.1 CHESS\images\Chess_tile_bl.png")).convert()
		self.white_bishop = pygame.transform.scale(self.white_bishop, (self.square_size,self.square_size))
		self.white_bishop.set_colorkey(VERDE)
		self.white_king = pygame.image.load(os.path.join(r"C:\Program files\Eusebio la doble Marca\M2.1 CHESS\images\Chess_tile_kl.png")).convert()
		self.white_king = pygame.transform.scale(self.white_king, (self.square_size,self.square_size))
		self.white_king.set_colorkey(VERDE)
		self.white_queen = pygame.image.load(os.path.join(r"C:\Program files\Eusebio la doble Marca\M2.1 CHESS\images\Chess_tile_ql.png")).convert()
		self.white_queen = pygame.transform.scale(self.white_queen, (self.square_size,self.square_size))
		self.white_queen.set_colorkey(VERDE)
		self.white_jilanko = pygame.image.load(os.path.join(r"C:\Program files\Eusebio la doble Marca\M2.1 CHESS\images\jilankoblanco.png")).convert()
		self.white_jilanko = pygame.transform.scale(self.white_jilanko, (self.square_size,self.square_size))
		self.white_jilanko.set_colorkey(VERDE)
		if self.estilo == 1:
			self.fondo = pygame.image.load(os.path.join(r"C:\Program files\Eusebio la doble Marca\M2.1 CHESS\images\paisaje1.jpg")).convert()
		elif self.estilo==2:
			self.fondo = pygame.image.load(os.path.join(r"C:\Program files\Eusebio la doble Marca\M2.1 CHESS\images\paisaje2.jpg")).convert()
		else:
			self.fondo = pygame.image.load(os.path.join(r"C:\Program files\Eusebio la doble Marca\M2.1 CHESS\images\paisaje3.png")).convert()

	def PrintMessage(self,message):
		#muestra la cadena donde salen los mensajes
		self.textBox.Add(message)
		self.textBox.Draw()

	def ConvertToScreenCoords(self,chessSquareTuple):
		#convierte a (row,col) chessSquare into the pixel location of the upper-left corner of the square
		(row,col) = chessSquareTuple
		screenX = self.boardStart_x + col*self.square_size - row*self.square_size
		screenY = self.boardStart_y + row*self.square_size + col*self.square_size
		#screenX1 = self.boardStart_x1 + col*self.square_size
		#screenY1 = self.boardStart_y1 + row*self.square_size
		return (screenX,screenY)

	def ConvertToChessCoords(self,screenPositionTuple):

		(X,Y) = screenPositionTuple
		row = 0
		col = 0
		if X>=25 and X<100 and Y>=330 and Y<430:
			row = 6
			col = 0
		elif X>=100 and X<150 and Y>=280 and Y<380:
			row = 5
			col = 0
		elif X>=100 and X<150 and Y>=380 and Y<480:
			row = 6
			col = 1
		elif X>=150 and X<200 and Y>=230 and Y<330:
			row = 4
			col = 0
		elif X>=150 and X<200 and Y>=330 and Y<430:
			row = 5
			col = 1
		elif X>=150 and X<200 and Y>=430 and Y<530:
			row = 6
			col = 2
		elif X>=200 and X<250 and Y>=180 and Y<280:
			row = 3
			col = 0
		elif X>=200 and X<250 and Y>=280 and Y<380:
			row = 4
			col = 1
		elif X>=200 and X<250 and Y>=380 and Y<480:
			row = 5
			col = 2
		elif X>=200 and X<250 and Y>=480 and Y<580:
			row = 6
			col = 3
		elif X>=250 and X<300 and Y>=130 and Y<230:
			row = 2
			col = 0
		elif X>=250 and X<300 and Y>=230 and Y<330:
			row = 3
			col = 1
		elif X>=250 and X<300 and Y>=330 and Y<430:
			row = 4
			col = 2
		elif X>=250 and X<300 and Y>=430 and Y<530:
			row = 5
			col = 3
		elif X>=250 and X<300 and Y>=530 and Y<630:
			row = 6
			col = 4
		elif X>=300 and X<350 and Y>=80 and Y<180:
			row = 1
			col = 0
		elif X>=300 and X<350 and Y>=180 and Y<280:
			row = 2
			col = 1
		elif X>300 and X<350 and Y>280 and Y<380:
			row = 3
			col = 2
		elif X>=300 and X<350 and Y>=380 and Y<480:
			row = 4
			col = 3
		elif X>=300 and X<350 and Y>=480 and Y<580:
			row = 5
			col = 4
		elif X>=300 and X<350 and Y>=580 and Y<680:
			row = 6
			col = 5
		elif X>=350 and X<400 and Y>=30 and Y<130:
			row = 0
			col = 0
		elif X>=350 and X<400 and Y>=130 and Y<230:
			row = 1
			col = 1
		elif X>=350 and X<400 and Y>=230 and Y<330:
			row = 2
			col = 2
		elif X>=350 and X<400 and Y>=330 and Y<430:
			row = 3
			col = 3
		elif X>=350 and X<400 and Y>=430 and Y<530:
			row = 4
			col = 4
		elif X>=350 and X<400 and Y>=530 and Y<630:
			row = 5
			col = 5
		elif X>=350 and X<400 and Y>=630 and Y<730:
			row = 6
			col = 6
		elif X>=400 and X<450 and Y>=80 and Y<180:
			row = 0
			col = 1
		elif X>=400 and X<450 and Y>=180 and Y<280:
			row = 1
			col = 2
		elif X>=400 and X<450 and Y>=280 and Y<380:
			row = 2
			col = 3
		elif X>=400 and X<450 and Y>=380 and Y<480:
			row = 3
			col = 4
		elif X>=400 and X<450 and Y>=480 and Y<580:
			row = 4
			col = 5
		elif X>=400 and X<450 and Y>=580 and Y<680:
			row = 5
			col = 6
		elif X>=450 and X<500 and Y>=130 and Y<230:
			row = 0
			col = 2
		elif X>=450 and X<500 and Y>=230 and Y<330:
			row = 1
			col = 3
		elif X>=450 and X<500 and Y>=330 and Y<430:
			row = 2
			col = 4
		elif X>=450 and X<500 and Y>=430 and Y<530:
			row = 3
			col = 5
		elif X>=450 and X<500 and Y>=530 and Y<630:
			row = 4
			col = 6
		elif X>=500 and X<550 and Y>=180 and Y<280:
			row = 0
			col = 3
		elif X>=500 and X<550 and Y>=280 and Y<380:
			row = 1
			col = 4
		elif X>=500 and X<550 and Y>=380 and Y<480:
			row = 2
			col = 5
		elif X>=500 and X<550 and Y>=480 and Y<580:
			row = 3
			col = 6
		elif X>=550 and X<600 and Y>=230 and Y<330:
			row = 0
			col = 4
		elif X>=550 and X<600 and Y>=330 and Y<430:
			row = 1
			col = 5
		elif X>=550 and X<600 and Y>=430 and Y<530:
			row = 2
			col = 6
		elif X>=600 and X<650 and Y>=280 and Y<380:
			row = 0
			col = 5
		elif X>=600 and X<650 and Y>=380 and Y<480:
			row = 1
			col = 6
		elif X>=650 and X<725 and Y>=330 and Y<430:
			row = 0
			col = 6
		elif X>=750 and X<850 and Y>=650 and Y<700:
			row = 8
			col = 8
		elif X>=850 and X<950 and Y>=650 and Y<700:
			row = 8
			col = 8
		elif X>=950 and X<1050 and Y>=650 and Y<700:
			row = 9
			col = 9
		return (row,col)


	def Draw(self,board,highlightSquares=[]):
		self.screen.blit(self.fondo,(0,0))#color de la pantalla de fondo(podra ser una imagen con blit)
		self.textBox.Draw()
		boardSize = len(board) #board should be square.  boardSize should be always 8 for chess, but I dislike "magic numbers" :)

     #DIBUJO DEL TABLERO EN ESTA SECCION

		#draw row/column labels around the edge of the board
		chessboard_obj = ChessBoard(0)#need a dummy object to access some of ChessBoard's methods....
		color = (255,255,255)#white
		antialias = 1

		"""#arriba y abajo - mostrando columnas_col
		for c in range(boardSize):
			for r in [-1,boardSize]:
				(screenX,screenY) = self.ConvertToScreenCoords((r,c))
				screenX = screenX + self.square_size#/2
				screenY = screenY + self.square_size#/2
				notation = chessboard_obj.ConvertToAlgebraicNotation_col(c)
				renderedLine = self.fontDefault.render(notation,antialias,color)
				self.screen.blit(renderedLine,(screenX,screenY))

		#izquierda y derecha - mostrando filas_row
		for r in range(boardSize):
			for c in [-1,boardSize]:
				(screenX,screenY) = self.ConvertToScreenCoords((r,c))
				screenX = screenX + self.square_size
				screenY = screenY + self.square_size
				notation = chessboard_obj.ConvertToAlgebraicNotation_row(r)
				renderedLine = self.fontDefault.render(notation,antialias,color)
				self.screen.blit(renderedLine,(screenX,screenY))"""

		#resaltado de cuadros de movimiento
		for square in highlightSquares:
			(screenX,screenY) = self.ConvertToScreenCoords(square)
			self.screen.blit(self.cyan_square,(screenX,screenY))

		#dibujar piezas
		for r in range(boardSize):
			for c in range(boardSize):
				(screenX,screenY) = self.ConvertToScreenCoords((r,c))
				(screenX,screenY) = (screenX+25,screenY+25)
				if board[r][c] == 'bP':
					self.screen.blit(self.black_pawn,(screenX,screenY))
				if board[r][c] == 'bR':
					self.screen.blit(self.black_rook,(screenX,screenY))
				if board[r][c] == 'bT':
					self.screen.blit(self.black_knight,(screenX,screenY))
				if board[r][c] == 'bB':
					self.screen.blit(self.black_bishop,(screenX,screenY))
				if board[r][c] == 'bQ':
					self.screen.blit(self.black_queen,(screenX,screenY))
				if board[r][c] == 'bK':
					self.screen.blit(self.black_king,(screenX,screenY))
				if board[r][c] == 'bJ':
					self.screen.blit(self.black_jilanko,(screenX,screenY))
				if board[r][c] == 'wP':
					self.screen.blit(self.white_pawn,(screenX,screenY))
				if board[r][c] == 'wR':
					self.screen.blit(self.white_rook,(screenX,screenY))
				if board[r][c] == 'wT':
					self.screen.blit(self.white_knight,(screenX,screenY))
				if board[r][c] == 'wB':
					self.screen.blit(self.white_bishop,(screenX,screenY))
				if board[r][c] == 'wQ':
					self.screen.blit(self.white_queen,(screenX,screenY))
				if board[r][c] == 'wK':
					self.screen.blit(self.white_king,(screenX,screenY))
				if board[r][c] == 'wJ':
					self.screen.blit(self.white_jilanko,(screenX,screenY))
                 #ascenso del mallku negro
				if board[4][0] == 'bJ': #4 y 0
					asc=Ascenso()
					(ascenso)=asc.GetGameSetupParams()
					cambio=ascenso
					board [4][0] = 'b'+cambio
				if board[5][1] == 'bJ': #5 y 1
					asc=Ascenso()
					(ascenso)=asc.GetGameSetupParams()
					cambio=ascenso
					board [5][1] = 'b'+cambio
				if board[6][2] == 'bJ':
					asc=Ascenso()
					(ascenso)=asc.GetGameSetupParams()
					cambio=ascenso
					board [6][2] = 'b'+cambio
                 #ascenso del mallku blanco
				if board[2][6] == 'wJ': #2 y 6
					asc=Ascenso()
					(ascenso)=asc.GetGameSetupParams()
					cambio=ascenso
					board [2][6] = 'w'+cambio
				if board[1][5] == 'wJ':
					asc=Ascenso()
					(ascenso)=asc.GetGameSetupParams()
					cambio=ascenso
					board [1][5] = 'w'+cambio
				if board[0][4] == 'wJ':
					asc=Ascenso()
					(ascenso)=asc.GetGameSetupParams()
					cambio=ascenso
					board [0][4] = 'w'+cambio
                    #enroque del rey
				if board[4][0] == 'wK' and board[3][0] == 'wR':
					board [3][0] = 'e'
					board [5][0] = 'wR'
				if board[6][2] == 'wK' and board[6][3] == 'wR':
					board [6][3] = 'e'
					board [6][1] = 'wR'
				if board[0][4] == 'bK' and board[0][3] == 'bR':
					board [0][3] = 'e'
					board [0][5] = 'bR'
				if board[2][6] == 'bK' and board[3][6] == 'bR':
					board [3][6] = 'e'
					board [1][6] = 'bR'
		pygame.display.flip()

	def EndGame(self,board):
		self.PrintMessage("Presione una tecla para salir.")
		self.Draw(board) #draw board to show end game status
		pygame.event.set_blocked(MOUSEMOTION)
		while 1:
			e = pygame.event.wait()
			if e.type is KEYDOWN:
				pygame.quit()
				sys.exit(0)
			if e.type is QUIT:
				pygame.quit()
				sys.exit(0)

	"""def Tablas(self,board):
		rey=0
		reyna=0
		alfil=0
		caballo=0
		torre=0
		jilanko=0
		peon=0
		rey1=0
		reyna1=0
		alfil1=0
		caballo1=0
		torre1=0
		jilanko1=0
		peon1=0
		for r in range(boardSize):
			for c in range(boardSize):
				if board [r][c] == 'wK':
					rey=rey+1
				if board [r][c] == 'wQ':
					reyna=reyna+1
				if board [r][c] == 'wB':
					alfil=alfil+1
				if board [r][c] == 'wT':
					caballo=caballo+1
				if board [r][c] == 'wR':
					torre=torre+1
				if board [r][c] == 'wJ':
					jilanko=jilanko+1
				if board [r][c] == 'wP':
					peon=peon+1
				if board [r][c] == 'bK':
					rey1=rey1+1
				if board [r][c] == 'bQ':
					reyna1=reyna1+1
				if board [r][c] == 'bB':
					alfil1=alfil1+1
				if board [r][c] == 'bT':
					caballo1=caballo1+1
				if board [r][c] == 'bR':
					torre1=torre1+1
				if board [r][c] == 'bJ':
					jilanko1=jilanko1+1
				if board [r][c] == 'bP':
					peon1=peon1+1
        return (rey,reyna,alfil,caballo,torre,jilanko,peon)"""

	def GetPlayerInput(self,board,currentColor,verify,s,sc,ayniB,ayniN):
		#returns ((from_row,from_col),(to_row,to_col))
		ayniBlanco=ayniB
		ayniNegro=ayniN
		fromSquareChosen = 0
		toSquareChosen = 0
		while not fromSquareChosen or not toSquareChosen:
			squareClicked = []
			pygame.event.set_blocked(MOUSEMOTION)
			e = pygame.event.wait()
			if e.type is KEYDOWN:
				if e.key is K_ESCAPE:
					fromSquareChosen = 0
					fromTuple = []
			if e.type is MOUSEBUTTONDOWN:
				(mouseX,mouseY) = pygame.mouse.get_pos()
				squareClicked = self.ConvertToChessCoords((mouseX,mouseY))
				if squareClicked[0]<0 or squareClicked[0]>9 or squareClicked[1]<0 or squareClicked[1]>9:
					squareClicked = [] #not a valid chess square
				elif squareClicked[0]==8 or squareClicked[1]==8:
					defs = exits()
					(confirm)=defs.confirmacion()
					if confirm == 1:
						if verify==0 :
							sc.send("empate")
							empatear=sc.recv(1024)
							if empatear=="aceptar":
							    em=empate()
							    (emp)=em.mostrarEmpate()
							    pygame.quit()
							    sc.close()
							    sys.exit(0)
							elif empatear=="no":
							    squareClicked = []
						elif verify==1:
							s.send("empate")
							empatar=sc.recv(1024)
							if empatar=="aceptar":
							    em=empate()
							    (emp)=em.mostrarEmpate()
							    pygame.quit()
							    s.close()
							    sys.exit(0)
							elif empatar=="no":
							    squareClicked = []
						else:
							em=empate()
							(emp)=em.mostrarEmpate()
							pygame.quit()
							sys.exit(0)
					elif confirm == 2:
						squareClicked = []
				elif squareClicked[0]==9 or squareClicked[1]==9:
					defs = exits()
					(confirm)=defs.confirmacion()
					if confirm == 1:
						if verify==0 :
							sc.send("salir")
							der=derrota()
							(derro)=der.mostrarDerrota()
							pygame.quit()
							sc.close()
							sys.exit(0)
						elif verify==1:
							s.send("salir")
							der=derrota()
							(derro)=der.mostrarDerrota()
							pygame.quit()
							s.close()
							sys.exit(0)
						else:
							der=derrota()
							(derro)=der.mostrarDerrota()
							pygame.quit()
							sys.exit(0)
					elif confirm == 2:
						squareClicked = []
			if e.type is QUIT: #the "x" kill button
				pygame.quit()
				sys.exit(0)



			if not fromSquareChosen and not toSquareChosen:
				self.Draw(board)
				if squareClicked != []:
					(r,c) = squareClicked
					if currentColor == 'negro' and 'b' in board[r][c]:
						if len(self.Rules.GetListOfValidMoves(board,currentColor,squareClicked,ayniBlanco,ayniNegro))>0:
							fromSquareChosen = 1
							fromTuple = squareClicked
					elif currentColor == 'blanco' and 'w' in board[r][c]:
						if len(self.Rules.GetListOfValidMoves(board,currentColor,squareClicked,ayniBlanco,ayniNegro))>0:
							fromSquareChosen = 1
							fromTuple = squareClicked

			elif fromSquareChosen and not toSquareChosen:
				possibleDestinations = self.Rules.GetListOfValidMoves(board,currentColor,fromTuple,ayniBlanco,ayniNegro)
				self.Draw(board,possibleDestinations)
				if squareClicked != []:
					(r,c) = squareClicked
					if squareClicked in possibleDestinations:
						toSquareChosen = 1
						toTuple = squareClicked
					elif currentColor == 'negro' and 'b' in board[r][c]:
						if squareClicked == fromTuple:
							fromSquareChosen = 0
						elif len(self.Rules.GetListOfValidMoves(board,currentColor,squareClicked,ayniBlanco,ayniNegro))>0:
							fromSquareChosen = 1
							fromTuple = squareClicked
						else:
							fromSquareChosen = 0 #piece is of own color, but no possible moves
					elif currentColor == 'blanco' and 'w' in board[r][c]:
						if squareClicked == fromTuple:
							fromSquareChosen = 0
						elif len(self.Rules.GetListOfValidMoves(board,currentColor,squareClicked,ayniBlanco,ayniNegro))>0:
							fromSquareChosen = 1
							fromTuple = squareClicked
						else:
							fromSquareChosen = 0
					else: #blank square or opposite color piece not in possible destinations clicked
						fromSquareChosen = 0

		return (fromTuple,toTuple)

	def GetClickedSquare(self,mouseX,mouseY):
		#test function
		print "User clicked screen position x =",mouseX,"y =",mouseY
		(row,col) = self.ConvertToChessCoords((mouseX,mouseY))
		if col <= 9 and col >= 0 and row <= 9 and row >= 0:
			print "  Chess board units row =",row,"col =",col

	def TestRoutine(self):
		#test function
		pygame.event.set_blocked(MOUSEMOTION)
		while 1:
			e = pygame.event.wait()
			if e.type is QUIT:
				return
			if e.type is KEYDOWN:
				if e.key is K_ESCAPE:
					pygame.quit()
					return
			if e.type is MOUSEBUTTONDOWN:
				(mouseX,mouseY) = pygame.mouse.get_pos()
				#x is horizontal, y is vertical
				#(x=0,y=0) is upper-left corner of the screen
				self.GetClickedSquare(mouseX,mouseY)




if __name__ == "__main__":
	#try out some development / testing stuff if this file is run directly
	testBoard = [['e','e','bP','bR','bT','bB','bK'],\
				 ['e','e','e','bP','bJ','bQ','bB'],\
				 ['wP','e','e','e','bP','bJ','bT'],\
				 ['wR','wP','e','e','e','bP','bR'],\
				 ['wT','wJ','wP','e','e','e','bP'],\
				 ['wB','wQ','wJ','wP','e','e','e'],\
				 ['wK','wB','wT','wR','wP','e','e']]

	validSquares = [(5,2),(1,1),(1,5),(7,6)]

	game = ChessGUI_pygame()
	game.Draw(testBoard,validSquares)
	game.TestRoutine()


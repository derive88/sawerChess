#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
 Project: Python Chess
 File name: ChessGameParams.py
 Description:  Creates a Tkinter dialog window to get game
	parameters.

 Copyright (C) 2009 Steve Osborne, srosborne (at) gmail.com
 http://yakinikuman.wordpress.com/
 """

from Tkinter import *
#from Tkinter import Tk,Frame,Label,Entry,Radiobutton,Button,StringVar,ANCHOR

class TkinterGameSetupParams:

    #self.cambio=1
	def __init__(self):
		self.root = Tk()
		self.root.title('Bienvenido a M2.1 ACHANK´ARA "(AA)"')
		self.root.iconbitmap(default=r'C:/Program files/Eusebio la doble Marca/M2.1 CHESS/images/icono.ico')
		self.root.geometry("600x120+300+300")
		self.frame = Frame(self.root)
		self.frame.pack()

		self.instructionMessage = StringVar()
		Label(self.frame, textvariable=self.instructionMessage).grid(row=0)
		self.instructionMessage.set("Ingrese las opciones de juego.")

		Label(self.frame, text="Nombre").grid(row=1,column=1)
		Label(self.frame, text="Tipo").grid(row=1,column=2)

		Label(self.frame, text="Jugador Principal").grid(row=2,column=0)
		self.entry_player1Name = Entry(self.frame)
		self.entry_player1Name.grid(row=2,column=1)
		self.entry_player1Name.insert(ANCHOR,"Atahualpa")

		self.tk_player1Type = StringVar()
		Radiobutton(self.frame, text="Humano",variable=self.tk_player1Type,value="humano").grid(row=2,column=2)
		Radiobutton(self.frame, text="Red(Servidor)",variable=self.tk_player1Type,value="server").grid(row=2,column=3)
		Radiobutton(self.frame, text="Red(Cliente)",variable=self.tk_player1Type,value="client").grid(row=2,column=4)
		#Radiobutton(self.frame, text="Offense AI",variable=self.tk_player1Type,value="offenseAI").grid(row=2,column=5)
		self.tk_player1Type.set("humano")

		Label(self.frame, text="Jugador Secundario").grid(row=3,column=0)
		self.entry_player2Name = Entry(self.frame)
		self.entry_player2Name.grid(row=3,column=1)
		self.entry_player2Name.insert(ANCHOR,"Huascar")

		"""self.tk_player2Type = StringVar()
		Radiobutton(self.frame, text="Humano",variable=self.tk_player2Type,value="humano").grid(row=3,column=2)
		Radiobutton(self.frame, text="Cliente(Red)",variable=self.tk_player2Type,value="client").grid(row=3,column=3)
		#Radiobutton(self.frame, text="Defense AI",variable=self.tk_player2Type,value="defenseAI").grid(row=3,column=4)
		#Radiobutton(self.frame, text="Offense AI",variable=self.tk_player2Type,value="offenseAI").grid(row=3,column=5)
		self.tk_player2Type.set("humano")"""


		b = Button(self.frame, text="Inicia el juego!", command=self.ok)
		b.grid(row=5,column=1)

	def ok(self):
		self.player1Type = self.tk_player1Type.get()
		self.player1Name = self.entry_player1Name.get()
		self.player2Name = self.entry_player2Name.get()
		#hardcoded so that player 1 is always white
		if self.player1Type == "humano":
			self.player1Color = "blanco"
			self.player2Color = "negro"
			self.player2Type = "humano"
		elif self.player1Type == "server":
			self.player1Color = "blanco"
			self.player2Color = "negro"
			self.player2Type = "client"
		elif self.player1Type == "client":
			self.player1Color = "negro"
			self.player2Color = "blanco"
			self.player2Type = "server"
		if self.player1Name != "" and self.player2Name != "":
			self.frame.destroy()
		else:
			#self.instructionMessage.set("Please input a name for both players!")
			if self.player1Name == "":
				self.entry_player1Name.insert(ANCHOR,"Atahualpa")
			if self.player2Name == "":
				self.entry_player2Name.insert(ANCHOR,"Huascar")

	def GetGameSetupParams(self):
		self.root.wait_window(self.frame) #waits for frame to be destroyed
		self.root.destroy() #noticed that with "text" gui mode, the tk window stayed...this gets rid of it.
		return (self.player1Name, self.player1Color, self.player1Type,
				self.player2Name, self.player2Color, self.player2Type)




if __name__ == "__main__":

	d = TkinterGameSetupParams()
	x = d.GetGameSetupParams()
	y = d.__init__()
	print x

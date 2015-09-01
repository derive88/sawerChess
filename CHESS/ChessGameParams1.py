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

class TGameSetupParams:

    #self.cambio=1
	def __init__(self):
		self.root = Tk()
		self.root.title('Bienvenido a M2.1 ACHANK´ARA "(AA)"')
		self.root.iconbitmap(default=r'C:/Program files/Eusebio la doble Marca/M2.1 CHESS/images/icono.ico')
		self.root.geometry("430x75+300+300")
		self.frame = Frame(self.root)
		self.frame.pack()

		self.instructionMessage = StringVar()
		Label(self.frame, textvariable=self.instructionMessage).grid(row=0)
		self.instructionMessage.set("Seleccione el tipo de tablero a usar:.")


		Label(self.frame, text="Tipo de tablero").grid(row=2,column=0)
		self.tablero = IntVar()
		Radiobutton(self.frame, text="Tablero 1",variable=self.tablero,value=1).grid(row=2,column=1)
		Radiobutton(self.frame, text="Tablero 2",variable=self.tablero,value=2).grid(row=2,column=2)
		Radiobutton(self.frame, text="Tablero 3",variable=self.tablero,value=3).grid(row=2,column=3)
		self.tablero.set(2)

		b = Button(self.frame, text="Cargar juego", command=self.ok)
		b.grid(row=3,column=1)

	def ok(self):
		#hardcoded so that player 1 is always white
		self.color_tablero = self.tablero.get()
		self.frame.destroy()

	def GetGameSetupParams(self):
		self.root.wait_window(self.frame) #waits for frame to be destroyed
		self.root.destroy() #noticed that with "text" gui mode, the tk window stayed...this gets rid of it.
		return (self.color_tablero)




if __name__ == "__main__":

	d = TGameSetupParams()
	x = d.GetGameSetupParams()
	y = d.__init__()
	print x

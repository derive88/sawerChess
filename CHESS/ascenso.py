#! /usr/bin/env python
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

class Ascenso:

	def __init__(self):
		self.root = Tk()
		self.root.title("Ascenso del Mallku")
		self.root.iconbitmap(default=r'C:/Program files/Eusebio la doble Marca/M2.1 CHESS/images/icono.ico')
		self.root.geometry("450x80+300+300")
		self.frame = Frame(self.root)
		self.frame.pack()


		self.instructionMessage = StringVar()
		Label(self.frame, textvariable=self.instructionMessage).grid(row=0)
		self.instructionMessage.set("Seleccione la pieza a cambiar")

		Label(self.frame, text="piezas posibles").grid(row=2,column=0)
		self.Ascender = StringVar()
		Radiobutton(self.frame, text="Pucara",variable=self.Ascender,value="R").grid(row=2,column=1)
		Radiobutton(self.frame, text="Llama",variable=self.Ascender,value="T").grid(row=2,column=2)
		Radiobutton(self.frame, text="Amauta",variable=self.Ascender,value="B").grid(row=2,column=3)
		Radiobutton(self.frame, text="Coya",variable=self.Ascender,value="Q").grid(row=2,column=4)
		self.Ascender.set("R")

		b = Button(self.frame, text="Aceptar", command=self.ok)
		b.grid(row=3,column=1)

	def ok(self):
		#hardcoded so that player 1 is always white
		self.ascenso = self.Ascender.get()
		self.frame.destroy()

	def GetGameSetupParams(self):
		self.root.wait_window(self.frame) #waits for frame to be destroyed
		self.root.destroy() #noticed that with "text" gui mode, the tk window stayed...this gets rid of it.
		return (self.ascenso)




if __name__ == "__main__":

	d = Ascenso()
	x = d.GetGameSetupParams()
	y = d.__init__()
	print x
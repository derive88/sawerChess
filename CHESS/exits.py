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

class exits:

	def __init__(self):
		self.root = Tk()
		self.root.title("Salir")
		self.root.iconbitmap(default=r'C:/Program files/Eusebio la doble Marca/M2.1 CHESS/images/icono.ico')
		self.root.geometry("200x50+400+300")
		self.frame = Frame(self.root)
		self.frame.pack()

		self.instructionMessage = StringVar()
		Label(self.frame, textvariable=self.instructionMessage).grid(row=0)
		self.instructionMessage.set("Seleccione Si para confirmar")


		#Label(self.frame, text="seleccione").grid(row=1,column=1)

		b = Button(self.frame, text="SI", command=self.si)
		b.grid(row=2,column=0)
		b = Button(self.frame, text="NO", command=self.no)
		b.grid(row=2,column=1)

	def si(self):
		#hardcoded so that player 1 is always white
		self.ascenso = 1
		self.frame.destroy()
	def no(self):
		#hardcoded so that player 1 is always white
		self.ascenso = 2
		self.frame.destroy()

	def confirmacion(self):
		self.root.wait_window(self.frame) #waits for frame to be destroyed
		self.root.destroy() #noticed that with "text" gui mode, the tk window stayed...this gets rid of it.
		return (self.ascenso)




if __name__ == "__main__":

	d = exits()
	x = d.confirmacion()
	y = d.__init__()
	print x
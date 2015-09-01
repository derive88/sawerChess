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

class conexion:

	def __init__(self):
		self.root = Tk()
		self.root.title("Conexion a red")
		self.root.geometry("700x700+250+20")
		self.frame = Frame(self.root)
		self.frame.pack()


		self.instructionMessage = StringVar()
		Label(self.frame, textvariable=self.instructionMessage).grid(row=0)
		self.instructionMessage.set("Seleccione el tipo de conexion a usar")

		Label(self.frame, text="Tipo de conexion").grid(row=2,column=0)
		self.conect = IntVar()
		Radiobutton(self.frame, text="Ser el Servidor",variable=self.conect,value=1).grid(row=2,column=1)
		Radiobutton(self.frame, text="Ser el Cliente",variable=self.conect,value=2).grid(row=2,column=2)
		self.conect.set(1)

		b = Button(self.frame, text="Aceptar", command=self.ok)
		b.grid(row=3,column=1)

	def ok(self):
		#hardcoded so that player 1 is always white
		self.conect = self.conect.get()
		self.frame.destroy()

	def datoConexion(self):
		self.root.wait_window(self.frame) #waits for frame to be destroyed
		self.root.destroy() #noticed that with "text" gui mode, the tk window stayed...this gets rid of it.
		return (self.conect)




if __name__ == "__main__":

	d = conexion()
	x = d.datoConexion()
	y = d.__init__()
	print x
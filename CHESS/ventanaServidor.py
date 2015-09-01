#! /usr/bin/env python

from Tkinter import *
import socket

class ventanaServer:

	def __init__(self):
		nombre_equipo = socket.gethostname()
		self.direccion = socket.gethostbyname(nombre_equipo)
		self.root = Tk()
		self.root.title("ESPERANDO CONEXION...")
		self.root.iconbitmap(default=r'C:/Program files/Eusebio la doble Marca/M2.1 CHESS/images/icono.ico')
		self.root.geometry("380x100+400+300")
		self.frame = Frame(self.root)
		self.frame.pack()

		self.instructionMessage = StringVar()
		Label(self.frame, textvariable=self.instructionMessage).grid(row=0)
		self.instructionMessage.set("Ingrese la clave en el cliente para iniciar la conexion")

		Label(self.frame, text="Clave").grid(row=1,column=0)

		self.entry_player1Name = Entry(self.frame)
		self.entry_player1Name.grid(row=2,column=0)
		self.entry_player1Name.insert(ANCHOR,self.direccion)


		b = Button(self.frame, text="Conectar", command=self.ok)
		b.grid(row=5,column=0)
		b = Button(self.frame, text="Cancelar", command=self.no)
		b.grid(row=5,column=1)

	def ok(self):
		self.player1Name = self.entry_player1Name.get()
		if self.player1Name != "" :
			self.frame.destroy()
		else:
			#self.instructionMessage.set("Please input a name for both players!")
			if self.player1Name == "":
				self.entry_player1Name.insert(ANCHOR,self.direccion)
	def no(self):
		self.player1Name = "0"
		self.frame.destroy()

	def GetipServer(self):
		self.root.wait_window(self.frame) #waits for frame to be destroyed
		self.root.destroy() #noticed that with "text" gui mode, the tk window stayed...this gets rid of it.
		return (self.player1Name)



if __name__ == "__main__":

	d = ventanaServer()
	x = d.GetipServer()
	y = d.__init__()
	print x

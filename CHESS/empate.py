#! /usr/bin/env python
from Tkinter import *
from PIL import ImageTk, Image
import os
#from Tkinter import Tk,Frame,Label,Entry,Radiobutton,Button,StringVar,ANCHOR
class empate:

	def __init__(self):
		self.root = Tk()
		self.root.title("Tablas-Empate")
		self.root.iconbitmap(default=r'C:/Program files/Eusebio la doble Marca/M2.1 CHESS/images/icono.ico')
		self.root.geometry("800x620+250+100")
		self.frame = Frame(self.root)
		self.frame.pack()


		self.img = ImageTk.PhotoImage(Image.open(r"C:\Program files\Eusebio la doble Marca\M2.1 CHESS\images\empate.jpg"))
		self.panel = Label(self.root, image = self.img)
		self.panel.pack(side = "bottom", fill = "both", expand = "yes")

		b = Button(self.frame, text="Aceptar", command=self.ok)
		b.grid(row=1,column=1)

	def ok(self):
		#hardcoded so that player 1 is always white
		self.fin = 1
		self.frame.destroy()

	def mostrarEmpate(self):
		self.root.wait_window(self.frame) #waits for frame to be destroyed
		self.root.destroy() #noticed that with "text" gui mode, the tk window stayed...this gets rid of it.
		return (self.fin)




if __name__ == "__main__":

	d = empate()
	x = d.mostrarEmpate()
	y = d.__init__()
	print x
"""root = Tk()
frame = Frame(root)
frame.pack()
img = ImageTk.PhotoImage(Image.open("images/victoria1.jpg"))
panel = Label(root, image = img)
panel.pack(side = "bottom", fill = "both", expand = "yes")
root.mainloop()
class victoria:
	def __init__(self):
		self.root = Tk()
		self.root.title("victoria")
		self.frame = Frame(self.root)
		self.frame.pack()
		self.img = ImageTk.PhotoImage(Image.open("images/victoria1.jpg"))
		self.panel = Label(self.root, image = self.img)
		self.panel.pack(side = "bottom", fill = "both", expand = "yes")

	def mostrarVictoria(self):
		self.root.wait_window(self.frame) #waits for frame to be destroyed
		self.root.destroy() #noticed that with "text" gui mode, the tk window stayed...this gets rid of it.
		return (self.fin)
if __name__ == "__main__":

	d = victoria()
	x = d.mostrarVictoria()
	y = d.__init__()
	print x"""

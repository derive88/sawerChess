from Tkinter import *
from PIL import ImageTk, Image
import os
#from Tkinter import Tk,Frame,Label,Entry,Radiobutton,Button,StringVar,ANCHOR
class derrota:

	def __init__(self):
		self.root = Tk()
		self.root.title("DERROTA")
		self.root.iconbitmap(default=r'C:/Program files/Eusebio la doble Marca/M2.1 CHESS/images/icono.ico')
		self.root.geometry("750x600+250+20")
		self.frame = Frame(self.root)
		self.frame.pack()


		self.img = ImageTk.PhotoImage(Image.open(r"C:\Program files\Eusebio la doble Marca\M2.1 CHESS\images\derrota.jpg"))
		self.panel = Label(self.root, image = self.img)
		self.panel.pack(side = "bottom", fill = "both", expand = "yes")

		b = Button(self.frame, text="Aceptar", command=self.ok)
		b.grid(row=1,column=1)

	def ok(self):
		#hardcoded so that player 1 is always white
		self.fin = 1
		self.frame.destroy()

	def mostrarDerrota(self):
		self.root.wait_window(self.frame) #waits for frame to be destroyed
		self.root.destroy() #noticed that with "text" gui mode, the tk window stayed...this gets rid of it.
		return (self.fin)




if __name__ == "__main__":

	d = derrota()
	x = d.mostrarDerrota()
	y = d.__init__()
	print x
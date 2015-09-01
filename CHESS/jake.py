from Tkinter import *
#from Tkinter import Tk,Frame,Label,Entry,Radiobutton,Button,StringVar,ANCHOR

class jake:

	def __init__(self):
		self.root = Tk()
		self.root.title("PELIGRO")
		self.root.iconbitmap(default=r'C:/Program files/Eusebio la doble Marca/M2.1 CHESS/images/icono.ico')
		self.root.geometry("450x50+300+300")
		self.frame = Frame(self.root)
		self.frame.pack()


		self.instructionMessage = StringVar()
		Label(self.frame, textvariable=self.instructionMessage).grid(row=0)
		self.instructionMessage.set("Acaba de ser puesto en JAQE solo podra mover las piezas para salir de JAQE")

		b = Button(self.frame, text="Aceptar", command=self.ok)
		b.grid(row=3,column=0)

	def ok(self):
		#hardcoded so that player 1 is always white
		self.ascenso = 1
		self.frame.destroy()

	def aviso(self):
		self.root.wait_window(self.frame) #waits for frame to be destroyed
		self.root.destroy() #noticed that with "text" gui mode, the tk window stayed...this gets rid of it.
		return (self.ascenso)




if __name__ == "__main__":

	d = jake()
	x = d.aviso()
	y = d.__init__()
	print x
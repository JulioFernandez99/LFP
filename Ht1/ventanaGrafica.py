import tkinter
from tkinter import *

class windowEstudiante:
    def __init__(self):
        self.app=Tk()
        self.app.title("LFP | Hoja de trabajo #1")
        self.frame=Frame(self.app,width=600,height=400)
        self.frame.config(bg="#09AEC4")
        self.frame.pack()
        self.campos()
        self.app.mainloop()

    def campos(self):

        self.noc=Label(self.frame,text="No. Carnet: 201902416")
        self.noc.config(font=("Arial",13),bg="#09AEC4")
        self.noc.place(x=210,y=100)

        self.name = Label(self.frame, text="Nombre: Julio Alfredo Fernandez Rodriguez")
        self.name.config(font=("Arial", 13),bg="#09AEC4")
        self.name.place(x=140, y=160)

        self.dato = tkinter.StringVar()
        self.campo = Entry(self.frame, textvariable=self.dato)
        self.campo.config(font=("Arial",10))
        self.campo.place(x=200,y=220)

        self.btn = Button(self.frame, text="Click", command=self.action)
        self.btn.place(x=360, y=215)


        self.msj=Label(self.frame)
        self.msj.place(x=200,y=270)
        self.msj.config(font=("Arial",20),foreground="#390673",bg="#09AEC4")

    def action(self):
        self.msj.config(text=self.dato.get())
        self.dato.set("")

if __name__=='__main__':
    w=windowEstudiante()
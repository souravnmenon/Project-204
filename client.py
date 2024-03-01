import socket
from tkinter import *
from threading import Thread
from PIL import ImageTk
import random

def setup():
  global SERVER, IP_ADDRESS, PORT

  IP_ADDRESS = "127.0.0.1"
  PORT = 6000

  SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  SERVER.connect((IP_ADDRESS, PORT))
  
  thread = Thread(target=recievedMsg)
  thread.start()

def askName():
  global canvas1
  global playerName, nameEntry, nameWindow
  cb = "Chalkboard SE"

  nameWindow = Tk()
  nameWindow.title("Tambola Board Game")
  nameWindow.geometry("800x688")

  scrW = nameWindow.winfo_screenwidth()
  scrH = nameWindow.winfo_screenheight()

  bg = ImageTk.PhotoImage(file = "./assets/background.bg")
  canvas1 = Canvas(nameWindow, width=500, height=500)
  canvas1.pack(fill="both", expand=True)
  canvas1.create_image(0, 0, image=bg, anchor="nw")
  canvas1.create_text(scrW/4.5, scrH/8, text="Enter Name", font=(cb,60), fill="#000")

  nameEntry = Entry(nameWindow, width=15, justify="center", font=(cb,30), bd=5, bg="#FFF")
  nameEntry.place(x=scrW/7, y=scrH/5.5)

  button = Button(nameWindow, text="Save", font=(cb,30), width=11, height=2, bd=3, bg="#80deea", command=saveName)
  button.place(x=scrW/6, y=scrH/4)

  nameWindow.resizable(True, True)
  nameWindow.mainloop()

def saveName():
  global SERVER
  global playerName, nameEntry, nameWindow

  playerName = nameEntry.get()
  nameEntry.delete(0,END)
  nameWindow.destroy()

  SERVER.send(playerName.encode())

def recievedMsg():
  pass
import tkinter as tk
import random
from tkinter import messagebox

mscreen=tk.Tk()


def get_name():
    givenname=str(nameentry.get())
    messagebox.showinfo("hello", givenname+" guess the number from 1-20!")


mscreen.geometry("500x300")
mscreen.configure(bg="white")
mscreen.title("Guess the number")


attempts=0
actualnumber=random.randint(1, 20)

def guessnumb():
    global actualnumber, attempts
    attempts=attempts+1
    attemptslabel.config(text="Attempts: "+str(attempts))
    getnumb=int(guessentry.get())
    
    if actualnumber>getnumb:
        messagebox.showinfo("incorrect", "guess higher!")

    elif actualnumber<getnumb:
        messagebox.showinfo("incorrect", "guess lower!")

    else:
        messagebox.showinfo("CORRECT", "You got it correct!")

    if attempts==4 and actualnumber!=getnumb:
        messagebox.showinfo("Lost", "You lost because you took the maximum attempts!")
        attempts=0
        actualnumber=random.randint(1, 20)
        nameentry.delete(0, tk.END)
        guessentry.delete(0, tk.END)

titlelabel=tk.Label(text="Welcome to our game!", width=20, height=1, bg="white", fg="black")
titlelabel.place(x=150, y=50)

attemptslabel=tk.Label(text="Attempts: "+str(attempts), width=20, height=1, bg="white", fg="black")
attemptslabel.place(x=150, y=250)

namelabel=tk.Label(text="What is your name?", width=20, height=1, bg="white", fg="black")
namelabel.place(x=0, y=150)

nameentry=tk.Entry(width=20, bg="white", fg="black")
nameentry.place(x=20, y=170)

guesslabel=tk.Label(text="Take a guess:", width=20, height=1, bg="white", fg="black")
guesslabel.place(x=-11, y=200)

guessentry=tk.Entry(width=20, bg="white", fg="black")
guessentry.place(x=100, y=200)

okbutton=tk.Button(text="OK", width=4, height=1, bg="grey", fg="black", command=get_name)
okbutton.place(x=250, y=160)

guessbutton=tk.Button(text="Guess", width=4, height=1, bg="grey", fg="black", command=guessnumb)
guessbutton.place(x=250, y=200)

mscreen.mainloop()
import tkinter as tk
import speech_recognition as sr
import pyaudio
from tkinter import messagebox



def speechtotext():
    recogniser=sr.Recognizer()
    with sr.Microphone() as source:
        try:

            audiodata=recogniser.listen(source)
            textdata=recogniser.recognize_google(audiodata)
            resultext.insert(tk.END, textdata)
        except sr.UnknownValueError:
            print("couldn't recognise voice")

def cleartext():
    resultext.delete("1.0", "end-1c")

def savetext():
    file=open("output.txt", "a")
    textdata=resultext.get("1.0", "end-1c")
    file.write(textdata)
    file.write("\n")
    file.close()
    messagebox.showinfo("Saved", "You text has been saved.")



mscreen=tk.Tk()
mscreen.geometry("700x500")
mscreen.configure(bg="black")
mscreen.title("Voice note pad")

recordbutton=tk.Button(text="click on me to start recording!", width=22, height=1, bg="blue", fg="black", command=speechtotext)
recordbutton.place(x=10, y=70)

cleartextbutton=tk.Button(text="clear text", width=20, height=1, bg="red", fg="black", command=cleartext)
cleartextbutton.place(x=500, y=100)

resultext=tk.Text(width=35, height=10,  bg="white", fg="black")
resultext.place(x=182, y=70)

Savebutton=tk.Button(text="Save this text", width=20, height=1, bg="green", fg="black", command=savetext)
Savebutton.place(x=500, y=70)

mscreen.mainloop()
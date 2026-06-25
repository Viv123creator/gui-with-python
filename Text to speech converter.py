import gtts 
import tkinter as tk
import pygame

pygame.mixer.init()



def convert():
    text2=text1.get("1.0", "end-1c")
    audio_file=gtts.gTTS(text=text2, lang="en", slow=False)
    audio_file.save("output.mp3")

def play():
    text2=text1.get("1.0", "end-1c")
    audio_file=gtts.gTTS(text=text2, lang="en", slow=False)
    audio_file.save("output.mp3")
    audio_file=pygame.mixer.music.load("output.mp3")
    pygame.mixer.music.play(1)
    

def stop():
    pygame.mixer.music.stop()


mainscreen=tk.Tk()
mainscreen.title("Text to speech converter")
mainscreen.geometry("800x800")
mainscreen.configure(bg="white")

l1=tk.Label(text="Text to speech converter app", width=40, height=2, bg="white", fg="black", font=(20))
l1.place(x=100, y=50)

l2=tk.Label(text="Enter the text", width=35, height=1, bg="white", fg="black", font=(13))
l2.place(x=0, y=150)

text1=tk.Text(width=20, height=5, bg="white", fg="black")
text1.place(x=290, y=150)

b1=tk.Button(text="Convert", width=20, height=1, bg="green", fg="black", command=convert)
b1.place(x=200, y=290)

b2=tk.Button(text="Play", width=20, height=1, bg="green", fg="black", command=play)
b3=tk.Button(text="Stop", width=20, height=1, bg="green", fg="black", command=stop)

b2.place(x=550, y=150)
b3.place(x=550, y=200)

mainscreen.mainloop()
import tkinter as tk
import datetime as dt

#Fetching the time
def show_time():
    current_time=dt.datetime.now()
    x=current_time.strftime("%I:%M:%S  %p")
    
    print(x)
    l2.config(text=x)
    l2.after(1000, show_time)

#Creating the screen
mainscreen=tk.Tk()
mainscreen.title("Digital clock")
mainscreen.geometry("500x500")
mainscreen.configure(bg="white")

#Creating the labels and output buttons
l1=tk.Label(text="Digital clock", width=20, height=1, bg="white", fg="black", font=(20))
l1.place(x=100, y=50)

b1=tk.Button(text="Show time: ", width=20, height=2, bg="green", fg="black", font=(20), command=show_time)
b1.place(x=100, y=100)

l2=tk.Label(width=20, height=2, bg="orange", fg="black", font=(20))
l2.place(x=100, y=190)













mainscreen.mainloop()
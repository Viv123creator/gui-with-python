import tkinter as tk

mscreen=tk.Tk()
canvas=tk.Canvas(width=800, height=750, bg="black")
canvas.place(x=0, y=50)

lastx=None
lasty=None

penwidth=2
pencolour="black"



def eraser():
    global pencolour
    pencolour="black"
    l1.select_clear(0, tk.END)



def paint(event):
    global lastx, lasty, penwidth, pencolour
    penwidth=int(s1.get())
    selectedindexes=l1.curselection()

    if selectedindexes:
        pencolour=l1.get(selectedindexes[0])

    lastx=event.x
    lasty=event.y

    if lastx and lasty:
        canvas.create_line(lastx, lasty, event.x, event.y, width=penwidth, fill=pencolour, capstyle="round", smooth=True)
    
    lastx=event.x
    lasty=event.y



mscreen.geometry("800x800")
mscreen.configure(bg="white")


colours=["red", "blue", "green", "yellow", "brown", "black", "light blue", "orange", "purple", "pink"]

l1=tk.Listbox(width=20, height=3)

for i in colours:
    l1.insert(tk.END, i) 

l1.place(x=160, y=0)

s1=tk.Scale(from_=0, to=10, orient=tk.HORIZONTAL)
s1.place(x=640, y=10)





Eraser=tk.Button(text="Duster", width=20, height=1, bg="white", fg="black", command=eraser)
Eraser.place(x=350, y=25)

canvas.bind("<B1-Motion>", paint)

mscreen.mainloop()
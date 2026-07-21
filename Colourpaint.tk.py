import tkinter as tk

#Creates screen
mscreen=tk.Tk()

canvas=tk.Canvas(width=1000, height=800, bg="white")
canvas.place(x=0, y=80)


lastx=None
lasty=None

penwidth=2
pencolour="black"

def brush():
    global penwidth
    s1.set(5)
    penwidth=5
    

def pen():
    global penwidth
    s1.set(2)
    penwidth=2


def eraser():
    global pencolour
    pencolour="white"
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
mscreen.title("Colour paint")
mscreen.configure(bg="black")

pen=tk.Button(text="pen", width=20, height=1, bg="purple", fg="black", command=pen)
pen.place(x=0, y=50)

brush=tk.Button(text="brush", width=20, height=1, bg="green", fg="black", command=brush)
brush.place(x=480, y=50)

eraser=tk.Button(text="eraser", width=20, height=1, bg="red", fg="black", command=eraser)
eraser.place(x=319, y=50)

colours=["red", "blue", "green", "yellow", "brown", "black", "light blue", "orange", "purple", "pink"]

l1=tk.Listbox(width=20, height=3)

for i in colours:
    l1.insert(tk.END, i)

l1.place(x=160, y=20)

s1=tk.Scale(from_=0, to=10, orient=tk.HORIZONTAL)
s1.place(x=640, y=38)

canvas.bind("<B1-Motion>", paint)










mscreen.mainloop()


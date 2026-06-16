import tkinter as tk



def convert_temprature():
    fahrenhiet=float(e1.get())
    celstep1=(fahrenhiet*1.8)
    celsius=(celstep1+32)
    t1.delete("1.0", tk.END)
    t1.insert("1.0", celsius)




mainscreen=tk.Tk()

mainscreen.title("Celsius to Fahrenhiet converter")
mainscreen.geometry("300x200")
mainscreen.configure(bg="white")




    


l1=tk.Label(text="Tempreture in celsius: ", width=20, height=1, bg="white", fg="black")
e1=tk.Entry(width=20, bg="white", fg="black")

l2=tk.Label(text="Tempreture in fahrenhiet= ", width=20, height=1, bg="white", fg="black")

t1=tk.Text(width=17, height=1, bg="white", fg="black")
b1=tk.Button(text="convert", width=20, height=1, bg="green", fg="black", command=convert_temprature)


l1.place(x=10, y=10)
e1.place(x=150, y=10)
b1.place(x=70, y=70)
l2.place(x=10, y=130)
t1.place(x=160, y=130)

mainscreen.mainloop()
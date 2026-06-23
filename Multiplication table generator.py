import tkinter as tk

def generate_table():
    number=int(e1.get())
    lb1.delete(0, tk.END)
    sr1=int(range1.get())
    for i in range(1, sr1+1):
        result=str(number)+"x"+str(i)+"="+str(number*i)
        lb1.insert(tk.END, result)




mainscreen=tk.Tk()
mainscreen.title("multiplication table generator")
mainscreen.geometry("500x500")
mainscreen.configure(bg="white")

range1=tk.IntVar()

l1=tk.Label(text="multiplication table generator", width=28, height=1, bg="white", fg="black", font=20)
l1.place(x=50, y=20)

l2=tk.Label(text="Enter a number:", width=20, height=1, bg="white", fg="black")
l2.place(x=40, y=50)

e1=tk.Entry(width=20, bg="white", fg="black")
e1.place(x=155, y=50)

b1=tk.Button(text="generate table", width=20, height=1, bg="green", fg="black", command=generate_table)
b1.place(x=140, y=140)

lb1=tk.Listbox(width=40, height=10)
lb1.place(x=100, y=200)

r1=tk.Radiobutton(text="10", variable=range1, value=10)
r1.place(x=300, y=200)
r2=tk.Radiobutton(text="20", variable=range1, value=20)
r2.place(x=300, y=300)
r3=tk.Radiobutton(text="30", variable=range1, value=30)
r3.place(x=300, y=400)




mainscreen.mainloop()
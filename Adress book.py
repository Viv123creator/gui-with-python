import tkinter as tk
from tkinter import messagebox



mscreen=tk.Tk()



def adddetails():
    name=nameentry.get()
    contact=contactnumbentry.get()
    adress=adresst.get("1.0", "end-1c")
    emailadress=emailentry.get()

    result="name: "+name+" , contactnumber: "+contact+" , adress: "+adress+" , emailadress: "+emailadress

    file=open("details.txt", "a")
    file.write(result)
    file.write("\n")
    file.close()

    lb1.insert(tk.END, result)
    messagebox.showinfo("Saved", "Your details have been saved.")






mscreen.title("Adress book")
mscreen.geometry("800x800")
mscreen.configure(bg="black")


l1=tk.Label(text="Welcome to Adress book", width=40, height=1, bg="white", fg="black", font=("Arial", 14))
l1.place(x=0, y=20)

Open=tk.Button(text="Open", width=20, height=1, bg="white", fg="black")
Open.place(x=450, y=20)

list1=[]



lb1=tk.Listbox(width=50, height=30)
lb1.place(x=50, y=100)

namelabel=tk.Label(text="Enter your name", width=20, height=1, bg="white", fg="black")
namelabel.place(x=400, y=100)

nameentry=tk.Entry(width=20, bg="white", fg="black")
nameentry.place(x=550, y=100)

clabel=tk.Label(text="contact number:", width=20, height=1, bg="white", fg="black")
clabel.place(x=400, y=150)

contactnumbentry=tk.Entry(width=20, bg="white", fg="black")
contactnumbentry.place(x=550, y=150)

adressl=tk.Label(text="Adress:", width=20, height=1, bg="white", fg="black")
adressl.place(x=400, y=200)

adresst=tk.Text(width=20, height=3, bg="white", fg="black")
adresst.place(x=550, y=200)

emailaddressl=tk.Label(text="Email adress:", width=20, height=1, bg="white", fg="black")
emailaddressl.place(x=400, y=290)

emailentry=tk.Entry(width=25, bg="white", fg="black")
emailentry.place(x=550, y=290)

addbutton=tk.Button(text="Add details", width=20, height=1, bg="Green", fg="black", command=adddetails)
addbutton.place(x=500, y=340)













mscreen.mainloop()
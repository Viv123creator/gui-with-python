import tkinter as tk


result=""

def calgrade():
    global result
    result=""

    name=ename.get()
    roll=eroll.get()
    mathg=int(emath.get())
    scienceg=int(escience.get())
    englishg=int(eenglish.get())

    result=result+name+"\n"
    result=result+roll+"\n"

    totalmarks=mathg+scienceg+englishg
    percentage=(totalmarks/300)*100
    print(percentage)
    result=result+"Your percentage is: "+str(percentage)


    if percentage>80 and percentage<100:
        grade="A"

    elif percentage>70 and percentage<=80:
        grade="B"

    elif percentage>60 and percentage<=70:
        grade="C"

    elif percentage>50 and percentage<=60:
        grade="D"

    elif percentage<=50:
        grade="F"

    print(grade)
    result=result+"\n"
    result=result+"Your grade is: "+(grade)+"\n"
    finalgrade.delete("1.0", "end-1c")
    finalgrade.insert("1.0", result)

def savetext():
    file=open("student.txt", "a")
    textdata=finalgrade.get("1.0", "end-1c")
    file.write(textdata)
    file.write("\n")
    file.close()


mscreen=tk.Tk()
mscreen.geometry("500x550")
mscreen.configure(bg="white")
mscreen.title("Grademaster 3000 - v1.0")

titlelabel=tk.Label(text="Student grading system", width=20, height=1, bg="white", fg="black", font=(10))
titlelabel.place(x=0, y=50)

namelabel=tk.Label(text="Name: ", width=20, height=1, bg="white", fg="black")
namelabel.place(x=-43, y=100)

rollabel=tk.Label(text="Roll no. :", width=20, height=1, bg="white", fg="black")
rollabel.place(x=-43, y=120)


mathlabel=tk.Label(text="Math grade: ", width=20, height=1, bg="white", fg="black")
mathlabel.place(x=-32, y=140)

sciencelabel=tk.Label(text="Science grade:", width=20, height=1, bg="white", fg="black")
sciencelabel.place(x=-32, y=160)

englishlabel=tk.Label(text="English grade: ", width=20, height=1, bg="white", fg="black")
englishlabel.place(x=-32, y=180)

ename=tk.Entry(width=20, bg="white", fg="black")
ename.place(x=100, y=100)

eroll=tk.Entry(width=20, bg="white", fg="black")
eroll.place(x=100, y=120)

emath=tk.Entry(width=20, bg="white", fg="black")
emath.place(x=100, y=140)

escience=tk.Entry(width=20, bg="white", fg="black")
escience.place(x=100, y=160)

eenglish=tk.Entry(width=20, bg="white", fg="black")
eenglish.place(x=100, y=180)

finalgrade=tk.Text(width=40, height=7, bg="white", fg="black")
finalgrade.place(x=40, y=250)

calgradebutton=tk.Button(text="Calculate grade", width=22, height=1, bg="blue", fg="black", command=calgrade)
calgradebutton.place(x=50, y=400)

savebutton=tk.Button(text="save student", width=22, height=1, bg="blue", fg="black", command=savetext)
savebutton.place(x=50, y=470)



mscreen.mainloop()





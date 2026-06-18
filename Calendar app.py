import tkinter as tk
import calendar as cal

def show_calendar():
    calendar_screen=tk.Tk()
    calendar_screen.geometry("550x600")
    calendar_screen.title("Year")
    calendar_screen.configure(bg="white")
    selected_year=int(s1.get())
    calendar_content=cal.calendar(selected_year)
    cal_lable=tk.Label(calendar_screen, text=calendar_content, bg="white", fg="black", font=("Consolas 10 bold"))
    cal_lable.grid(row=5, column=2, padx=20)
    calendar_screen.mainloop()

mainscreen=tk.Tk()

mainscreen.title("Calendar")
mainscreen.geometry("500x500")
mainscreen.configure(bg="white")

l1=tk.Label(text="Year:", width=20, height=1, bg="white", fg="black", font=14)
l1.place(x=-40, y=20)

s1=tk.Spinbox(width=20, from_=1950, to=3000)

b1=tk.Button(text="Show year", width=20, height=1, bg="green", fg="black", command=show_calendar)


b1.place(x=100, y=100)
s1.place(x=100, y=26)


mainscreen.mainloop()
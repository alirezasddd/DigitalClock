from tkinter import *
import time

window = Tk()
window.title("digital clock")
window.geometry("600x170")


def clock():
    hour = time.strftime("%I")
    minute = time.strftime("%M")
    second = time.strftime("%S")
    am_pm = time.strftime("%p")
    zone = time.strftime("%Z")

    mytext = hour + ":" + minute + ":" + second + "  " + am_pm
    mytext2 = zone
    mylabel.config(text=mytext)
    mylabel2.config(text=mytext2)
    mylabel.after(1000, clock)


mylabel = Label(window, text="", font=(
    'arial', 72), fg="silver", bg="black")
mylabel.pack()
mylabel2 = Label(window, text="", font=("Arial", 24))
mylabel2.pack()

clock()
window.mainloop()

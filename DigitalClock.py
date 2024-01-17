from tkinter import *
import time

window = Tk()
window.title("digital clock")
window.geometry("600x150")


def clock():
    hour = time.strftime("%I")
    minute = time.strftime("%M")
    second = time.strftime("%S")
    am_pm = time.strftime("%p")
    mytext = hour + ":" + minute + ":" + second + "  " + am_pm
    mylabel.config(text=mytext)
    mylabel.after(1000, clock)


mylabel = Label(window, text="", font=(
    'arial', 72), fg="silver", bg="black")
mylabel.pack()

clock()
window.mainloop()

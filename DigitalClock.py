from tkinter import *
import time

window = Tk()
window.title("digital clock")
window.geometry("600x400")


def clock():
    hour = time.strftime("%H")
    minute = time.strftime("%M")
    second = time.strftime("%S")
    mytext = hour + ":" + minute + ":" + second
    mylabel.config(text=mytext)
    mylabel.after(1000, clock)


mylabel = Label(window, text="", font=(
    'arial', 72), fg="white", bg="blue")
mylabel.pack()

clock()
window.mainloop()

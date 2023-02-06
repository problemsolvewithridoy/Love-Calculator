# Python Tkinter GUI based "LOVE CALCULATOR" by "Problem solve with Ridoy"

import tkinter
from tkinter import *
import random
from PIL import ImageTk, Image

root = Tk()
root.geometry('400x240')
root.title('Love Calculator')

img = (Image.open("love.png"))
image1 = img.resize((100, 100), Image.ANTIALIAS)
test = ImageTk.PhotoImage(image1)


label = tkinter.Label(image=test)
label.image = test

label.pack()


def calculate_love():
    st = '0123456789'
    digit = 2
    temp = "".join(random.sample(st, digit))
    result.config(text=temp)

heading = Label(root, text='Love Calculator made by "Problem solve with Ridoy"')
heading.pack()

slot1 = Label(root, text="Enter Your Name:")
slot1.pack()
name1 = Entry(root, border=5)
name1.pack()

slot2 = Label(root, text="Enter Your Partner Name:")
slot2.pack()
name2 = Entry(root, border=5)
name2.pack()

bt = Button(root, text="Calculate", height=1, width=7, command=calculate_love)
bt.pack()

result = Label(root, text='Love Percentage between both of You:')
result.pack()

root.mainloop()

#If you have any confusion, feel free to contact me https://www.facebook.com/problemsolvewithridoy/
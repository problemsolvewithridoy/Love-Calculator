
# Love Calculator

This is a Love Calculator project written in Python with an amazing GUI using the tkinter library. The project asks the user to input their name and the name of their crush, and then calculates a love percentage based on a simple algorithm. The result is displayed on the GUI, along with a funny message based on the love percentage.

The project is a great way to practice your Python programming skills, especially if you're interested in creating GUI applications. The code is well-commented and easy to understand, so it's a good starting point for beginners who want to learn more about Python and GUI development.

Feel free to download the code and customize it to your liking. If you find any bugs or have suggestions for improvement, please open an issue on the repository. Happy coding!


To make this project you need to follow this step:-










## Installation

Install package with pip

```bash
  pip install tkinter

```
    
## Deployment

To deploy this project run

```bash
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
```


## Output



![output](https://user-images.githubusercontent.com/123636419/216825689-6a3baf8f-54c3-4099-aa8c-737e5ba8dec2.PNG)



## You can follow me

Facebook:- https://www.facebook.com/problemsolvewithridoy/

Linkedin:- https://www.linkedin.com/in/ridoyhossain/

YouTube:- https://www.youtube.com/@problemsolvewithridoy

If you have any confusion, please feel free to contact me. Thank you


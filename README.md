# Python-Clock
A clock written in Python using Tkinter

## About
A simple program that shows the current date and time.

## Attention
In the source code you will notice this piece of code:
```
import os
os.environ['TCL_LIBRARY'] = r'C:\Users\maxcomputer\AppData\Local\Programs\Python\Python38-32\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Users\maxcomputer\AppData\Local\Programs\Python\Python38-32\tcl\tk8.6'
```
There is a mysterious! problem with my computer that i can't figure it out. In my computer, any code that has `tkinter` module pops a tcl error in console like this => `This probably means that Tcl wasn't installed properly.` I digged the internet to find a solution for the problem. Finally, I found a solution in Youtube.

If you have the same problem like mine, check out [solution](https://www.youtube.com/watch?v=TxpZopNkj7c).

If not, remove that part of the code.

## Screenshot
![clock](https://user-images.githubusercontent.com/124906353/220553936-9b4ab233-6555-49dd-8690-dc20c1b88609.PNG)

### Modules used:
* [datetime](https://docs.python.org/3/library/datetime.html?highlight=date#module-datetime)
* [time](https://docs.python.org/3/library/time.html?highlight=time#module-time)
* [tkinter](https://docs.python.org/3/library/tkinter.html?highlight=tkinter#module-tkinter)

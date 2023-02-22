import os
import tkinter as tk
import datetime
import time
os.environ['TCL_LIBRARY'] = r'C:\Users\maxcomputer\AppData\Local\Programs\Python\Python38-32\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Users\maxcomputer\AppData\Local\Programs\Python\Python38-32\tcl\tk8.6'

root = tk.Tk()
root.title("Clock")
root.geometry("300x300")
root.resizable(False, False)
root.configure(bg='black')

clock_icon = root.iconbitmap(r"H:\Bazargan_Dev\Programming\Python_Workspace\FunProject\Python_Clock\ClockIcon.ico")

header = tk.Label(root, text="Python Clock", background='black', foreground='white', font=('Arial', 30, 'bold'))
header.grid(row=0, column=1, pady=20)

nameTime = tk.Label(root, text="Time", background='black', foreground='white', font=('Arial', 15, 'bold'))
nameTime.grid(row=1, column=1)

clock_label = tk.Label(root, background='black', foreground='red', font=('Arial', 30, 'bold'))
clock_label.grid(row=2, column=1, padx=30)

nameDate = tk.Label(root, text="Date", background='black', foreground='white', font=('Arial', 15, 'bold'))
nameDate.grid(row=3, column=1)

date_label = tk.Label(root, text=datetime.datetime.today().strftime('%Y.%m.%d'), background='black', foreground='red', font=('Arial', 30, 'bold'))
date_label.grid(row=4, column=1, padx=30)

def UpdateLabel():
    CurrentTime = time.strftime("%H:%M:%S %p")
    clock_label.configure(text=CurrentTime)
    clock_label.after(80, UpdateLabel)

UpdateLabel()

root.mainloop()
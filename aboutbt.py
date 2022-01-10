# To import a specific Python file at 'runtime' with a known name.
import sys
import os

import tkinter as tk
import tkinter.ttk as ttk
from ttkthemes import ThemedStyle



def about():
    pic1 = tk.PhotoImage(file='icon2.png')
    pic2 = tk.PhotoImage(file='about.png')
    pic3 = tk.PhotoImage(file='icon3.png')
    about = tk.Toplevel()
    about.configure(bg="white")
    about.title("About")
    about.geometry("400x300")
    about.resizable(False, False)
    about.iconphoto(False, pic1)

    style = ThemedStyle(about)
    style.theme_use('arc')

    Ticon = ttk.Label(about, image=pic3, borderwidth=0, background="white")
    Ticon.place(relx=0.1, rely=0.1, height=100, width=100)

    Tlabel5 = ttk.Label(about)
    Tlabel5.place(relx=0.1, rely=0.5, height=100, width=350)
    Tlabel5.configure(background="white")
    Tlabel5.configure(justify='left')
    Tlabel5.configure(wraplength=330, text='This program was created as semester project for my python classes. The issue given was very simple, so I decided to make a simple window app for it.')

    Tlabel6 = ttk.Label(about)
    Tlabel6.place(relx=0.4, rely=0.2, height=40, width=400)
    Tlabel6.configure(background="white", text='Projekt "Koło"')
    Tlabel6.configure(justify='center', font=("default", 25))

    Tlabel7 = ttk.Label(about)
    Tlabel7.place(relx=0.75, rely=0.9, height=15, width=100)
    Tlabel7.configure(background="white")
    Tlabel7.configure(text='Pre-release 1.0')


    #about.focus_force()
    #about.bell()

    about.mainloop()



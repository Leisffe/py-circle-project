# To import a specific Python file at 'runtime' with a known name.
import sys
import os

import tkinter as tk
import tkinter.ttk as ttk
from ttkthemes import ThemedStyle
from itertools import product
from tkinter import filedialog

from aboutbt import *

app = tk.Tk()

pic1 = tk.PhotoImage(file='icon2.png')
pic2 = tk.PhotoImage(file='about.png')

def start_gui():
    app.configure(bg="white")
    app.title("Projekt")
    app.geometry("300x450")
    app.resizable(False, False)
    app.iconphoto(False, pic1)

    style = ThemedStyle(app)
    style.theme_use('arc')

    app.mainloop()

def quit():
    app.destroy()


def fileinput():
    userfile = filedialog.askopenfilename(initialdir="/home/", title="Wybierz plik", filetypes=(("Plik tekstowy", "*.txt"),("Wszystkie pliki", "*.*")))
    file = open(userfile, 'r')
    textinput = file.read()
    TEntry1.delete(0, 100)
    TEntry1.insert(0, textinput)

wholeframe = 1

def userinput():
    # Walidacja czy liczba
    try:
        assert float(TEntry1.get()) > 0
        x = y = getinput = float(TEntry1.get())
    except ValueError:
        errormsg1 = 'Error: Nie została podana liczba!' #error 1
        #tk.showinfo("ValueError!")
        Toutput.configure(text=errormsg1, anchor='c', wraplength=290)
    except AssertionError:
        errormsg2 = 'Error: Liczba musi być dodatnia!'
        Toutput.configure(text=errormsg2, anchor='c', wraplength=290)

    def points_in_circle(radius):
        for x, y in product(range(int(radius) + 1), repeat=2):
            if x ** 2 + y ** 2 <= radius ** 2:
                yield from set(((x, y), (x, -y), (-x, y), (-x, -y),))

    lista = list(points_in_circle(x))
    amount = len(lista)

    Toutput.configure(text=lista, anchor='nw', wraplength=290)

    total = ("Liczba punktów całkowitych: {}".format(amount))

    Toutput2.configure(text=total, anchor='nw', wraplength=290)

    global wholeframe
    wholeframe = ("{}\n\n{}".format(lista, total))

def copytoclipboard():
    app.clipboard_clear()
    app.clipboard_append(wholeframe)



# Buttons


# Label1

Tlabel1 = ttk.Label(app)
Tlabel1.place(relx=0.403, rely=0.111, height=20, width=70)
Tlabel1.configure(background="white")
Tlabel1.configure(justify='center')
Tlabel1.configure(text='Podaj r koła')

# User input
TEntry1 = ttk.Entry(app)
TEntry1.place(relx=0.3, rely=0.156, relheight=0.047, relwidth=0.42)
TEntry1.configure(takefocus="")
TEntry1.configure(cursor="xterm")

# Zaladuj

TButton5 = ttk.Button(app)
TButton5.place(relx=0.167, rely=0.222, height=28, width=96)
TButton5.configure(takefocus="")
TButton5.configure(text='''Załaduj z txt''')
TButton5.configure(command=fileinput)


# Oblicz
TButton4 = ttk.Button(app)
TButton4.place(relx=0.533, rely=0.222, height=28, width=96)
TButton4.configure(takefocus="")
TButton4.configure(text='''Oblicz''')
TButton4.configure(command=userinput)


# Frame

Toutput = ttk.Label(app)
Toutput.place(relx=0.01, rely=0.305, height=250, width=294)
Toutput.configure(background="#e3e3e3")
Toutput.configure(text='', anchor='nw')

# Frame2
Toutput2 = ttk.Label(app)
Toutput2.place(relx=0.01, rely=0.843, height=20, width=294)
Toutput2.configure(background="#e3e3e3")
Toutput2.configure(text='', anchor='nw')

# Kopiuj

Tbutton3 = ttk.Button(app)
Tbutton3.place(relx=0.167, rely=0.911, height=28, width=96)
Tbutton3.configure(text='Kopiuj wynik')
Tbutton3.configure(command=copytoclipboard)


# Exit button
Tbutton2 = ttk.Button(app, command=quit)
Tbutton2.place(relx=0.533, rely=0.911, height=28, width=96)
Tbutton2.configure(takefocus="")
Tbutton2.configure(text='Exit')

# About button

Tbutton1 = tk.Button(app, image=pic2, command=about, borderwidth=0, background="#f4f4f4")
Tbutton1.place(relx=0.04, rely=0.022, height=30, width=30)


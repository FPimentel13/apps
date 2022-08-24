import re
from tkinter import *


class Calculator:
    arg2 = None
    disp = None
    window = None
    buttons = {}

    def __init__(self):
        self.arg2 = None
        self.window = Tk()
        self.window.title("Calculator")
        self.window.config(bg='#FFFFFF') #color
        self.window.geometry("200x300")

        root = Frame(self.window)

        self.gridcreate(root)

        root.columnconfigure(tuple(range(4)), weight=1)
        root.rowconfigure(tuple(range(5)), weight=1)
        root.pack(fill="both",expand=True)

        root.bind("<Configure>", self.size_change)
        self.window.bind('<KeyPress>', self.onKeyPress)
        self.window.mainloop()

    def change(self, arg):
        disp = self.disp
        disp.config(state=NORMAL)
        if arg == "c":
            disp.delete(0,END)
        elif arg == "=":
            try:
                res = int(eval(disp.get()))
                disp.delete(0,END)
                disp.insert(0,res)
            except SyntaxError:
                disp.delete(0,END)
                disp.insert(0,"Syntax Error")
            except Exception:
                disp.delete(0,END)
                disp.insert(0,"Math Error")
        else:
            if self.arg2 == "=" and type(arg) == int:
                disp.delete(0,END)
            disp.insert(END,arg)
        disp.config(state="readonly")
        self.arg2 = arg

    def gridcreate(self, root):
        self.disp = Entry(root, state="readonly", readonlybackground="white")
        self.disp.grid(column=0, row=0, columnspan=4, sticky='nesw')

        # row1
        seven = Button(root, text="7", command=lambda : self.change(7))
        seven.grid(column=0,row=1, sticky='nesw')
        self.buttons["seven"] = seven

        eight = Button(root, text="8", command=lambda : self.change(8))
        eight.grid(column=1,row=1, sticky='nesw')
        self.buttons["eight"] = eight

        nine = Button(root, text="9", command=lambda : self.change(9))
        nine.grid(column=2,row=1, sticky='nesw')
        self.buttons["nine"] = nine

        div = Button(root, text="÷", command=lambda : self.change("/"))
        div.grid(column=3,row=1, sticky='nesw')
        self.buttons["div"] = div

        # row2
        four = Button(root, text="4", command=lambda : self.change(4))
        four.grid(column=0,row=2, sticky='nesw')
        self.buttons["four"] = four

        five = Button(root, text="5", command=lambda : self.change(5))
        five.grid(column=1,row=2, sticky='nesw')
        self.buttons["five"] = five

        six = Button(root, text="6", command=lambda : self.change(6))
        six.grid(column=2,row=2, sticky='nesw')
        self.buttons["six"] = six

        mult = Button(root, text="x", command=lambda : self.change("*"))
        mult.grid(column=3,row=2, sticky='nesw')
        self.buttons["mult"] = mult

        # row3
        three = Button(root, text="3", command=lambda : self.change(3))
        three.grid(column=0,row=3, sticky='nesw')
        self.buttons["three"] = three

        two = Button(root, text="2", command=lambda : self.change(2))
        two.grid(column=1,row=3, sticky='nesw')
        self.buttons["two"] = two

        one = Button(root, text="1", command=lambda : self.change(1))
        one.grid(column=2,row=3, sticky='nesw')
        self.buttons["one"] = one

        min = Button(root, text="-", command=lambda : self.change("-"))
        min.grid(column=3,row=3, sticky='nesw')
        self.buttons["min"] = min

        # row4
        c = Button(root, text="c", command=lambda : self.change("c"))
        c.grid(column=0,row=4, sticky='nesw')
        self.buttons["c"] = c

        zero = Button(root, text="0", command=lambda : self.change(0))
        zero.grid(column=1,row=4, sticky='nesw')
        self.buttons["zero"] = zero

        eq = Button(root, text="=", command=lambda : self.change("="))
        eq.grid(column=2,row=4, sticky='nesw')
        self.buttons["eq"] = eq

        plus = Button(root, text="+", command=lambda : self.change("+"))
        plus.grid(column=3,row=4, sticky='nesw')
        self.buttons["plus"] = plus

    def size_change(self, _):
        self.window.update()
        self.disp.config(font=('Candara',int(self.window.winfo_height()/20)))
        for but in self.buttons.values():
            but.config(font=('Candara',int(self.window.winfo_height()/20)))

    def onKeyPress(self, event):
        if event.char.isnumeric() or event.char == '/' or event.char == '*' or event.char == '+' or event.char == '-' or event.char == '=' or event.char == 'c':
            self.change(event.char)
        elif event.char == '\r':
            self.change("=")
        elif event.char == '\x08':
            self.disp.config(state=NORMAL)
            if self.arg2 == "=":
                self.disp.delete(0, END)
            else:
                self.disp.delete(len(self.disp.get())-1, END)
            self.disp.config(state="readonly")

Calculator() 
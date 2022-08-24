from random import randint
from tkinter import *

class Sudoku:
    root = None
    table = []
    def __init__(self):
        root = Tk()
        root.title('Model Definition')
        root.geometry('{}x{}'.format(460, 350))
        self.root = root
        
        # create all of the main containers
        top_frame = Frame(root)
        center = Frame(root, bg='gray2')
        btm_frame = Frame(root)
        btm_frame2 = Frame(root)

        # layout all of the main containers
        root.grid_rowconfigure(1, weight=1)
        root.grid_columnconfigure(0, weight=1)

        top_frame.grid(row=0, sticky="ew")
        center.grid(row=1, sticky="nsew")
        btm_frame.grid(row=3, sticky="ew")
        btm_frame2.grid(row=4, sticky="ew")

        # create the widgets for the top frame
        model_label = Label(top_frame, text='Sudoku')

        # layout the widgets in the top frame
        model_label.grid(row=0, columnspan=3)

        # create the center widgets
        center.grid_rowconfigure(0, weight=1)
        center.grid_columnconfigure(1, weight=1)

        ctr_left = Frame(center, width=100, height=190)
        ctr_mid = Frame(center, width=250, height=190, padx=3, pady=3)
        ctr_right = Frame(center, width=100, height=190, padx=3, pady=3)

        ctr_left.grid(row=0, column=0, sticky="ns")
        ctr_mid.grid(row=0, column=1, sticky="nsew")
        ctr_right.grid(row=0, column=2, sticky="ns")

        # create the widgets for the bottom frame
        bottom_label = Label(btm_frame, text='random')
        bottom_label2 = Label(btm_frame2, text='random2')
        bottom_label.grid(row=0, columnspan=3)
        bottom_label2.grid(row=0, columnspan=3)

        # create the grid
        frame_mid = Frame(ctr_mid, relief="solid", highlightthickness=3, highlightbackground="black", highlightcolor="black")
        frame_mid.columnconfigure(tuple(range(3)), weight=1)
        frame_mid.rowconfigure(tuple(range(3)), weight=1)
        frame_mid.pack(fill="both",expand=True)

        table = []
        for x in range(3):
            for y in range(3):
                frame_b = Frame(frame_mid)
                frame = Frame(frame_b, relief="solid", highlightthickness=1, highlightcolor="black")

                for a in range(3):
                    for b in range(3):
                        cell = Entry(frame, state="readonly", readonlybackground="white")
                        cell.grid(row=a, column=b, sticky='nsew')

                        table.append(cell)

                frame.columnconfigure(tuple(range(3)), weight=1)
                frame.rowconfigure(tuple(range(3)), weight=1)
                frame.pack(fill="both",expand=True)

                frame_b.grid(row=x, column=y, sticky='nsew')

        self.table = table
        root.bind('<KeyPress>', self.onKeyPress)
        root.mainloop()

    def onKeyPress(self, event):
        list = str(self.root.focus_get()).split(".")

        elem1 = list[4].replace('!frame','')
        if elem1 == '':
            elem1 = 1
        else:
            elem1 = int(elem1)

        elem2 = list[6].replace('!entry','')
        if elem2 == '':
            elem2 = 1
        else:
            elem2 = int(elem2)

        disp = self.table[elem1*elem2-1]
        if disp["state"] != DISABLED:
            disp.config(state=NORMAL)
            if event.char.isnumeric() and event.char != '0':
                disp.delete(0, END)
                disp.insert(0, event.char)
            elif event.char == '\x08' or event.char == '0':
                disp.delete(0, END)
            disp.config(state="readonly")

    def load_sudoku(self, num=-1):
        if num > 0:
            num = randint(0,10) * 0 # DEL THIS

        # Load list here
        list = []
        grid =[
            [7, 8, 0, 4, 0, 0, 1, 2, 0],
            [6, 0, 0, 0, 7, 5, 0, 0, 9],
            [0, 0, 0, 6, 0, 1, 0, 7, 8],
            [0, 0, 7, 0, 4, 0, 2, 6, 0],
            [0, 0, 1, 0, 5, 0, 9, 3, 0],
            [9, 0, 4, 0, 6, 0, 0, 0, 5],
            [0, 7, 0, 3, 0, 0, 0, 1, 2],
            [1, 2, 0, 0, 0, 7, 4, 0, 0],
            [0, 4, 9, 2, 0, 6, 0, 0, 7]
        ]
        list.append(grid)

        sudoku = list[num]


Sudoku()
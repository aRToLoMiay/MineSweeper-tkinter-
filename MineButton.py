import tkinter as tk
from enum import Enum


class MineButton(tk.Button):
    colors = {
        0: "#D3D3D3",  # light gray
        1: "#0000FF",  # blue
        2: "#008000",  # green
        3: "#FF0000",  # red
        4: "#191970",  # midnight blue
        5: "#A52A2A",  # brown
        6: "#40E0D0",  # turquoise
        7: "#000000",  # black
        8: "#FFFFFF",  # white
    }
    c_background = "#D3D3D3"  # light gray
    c_mine = "#000000"  # black
    s_mine = '╳'

    def __init__(self, master=None, row: int = 0, column: int = 0, *args, **kwargs):
        super(MineButton, self).__init__(
            master,
            width=3,
            font="Calibri 15 bold",
            background="#F0F0F0",
            *args,
            **kwargs,
        )
        self.isMine = False
        self.isChecked = False
        self.count = 0
        self.row = row
        self.column = column
        self.grid(row=row, column=column)

    def __repr__(self):
        # In this function we can redefine output to console in print(MineButton)
        return f"<MineButton - {self.isMine}>"

    def refresh(self):
        self.isMine = False
        self.count = 0
        self.config(
            width=3,
            font="Calibri 15 bold",
            disabledforeground = '#000000',
            text="",
            relief=tk.RAISED,
            background="#F0F0F0",
            state="active",
        )

    def click(self):
        self.isChecked = True
        if self.isMine:
            self.config(text="*", background="red", disabledforeground="#000000")
        else:
            color = MineButton.colors.get(self.count, MineButton.c_background)
            self.config(
                text=str(self.count),
                background=MineButton.c_background,
                disabledforeground=color,
            )
        self.config(state="disabled", relief=tk.SUNKEN)

    def rclick(self):
        if not self.isChecked:
            self.config(text=MineButton.s_mine, state='disabled')
            self.isChecked = True
            return 1
        elif self['text'] == MineButton.s_mine:
            self.config(text='', state='active')
            self.isChecked = False
            return -1
        return 0

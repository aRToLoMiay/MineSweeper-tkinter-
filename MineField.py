import tkinter as tk

from random import shuffle
from tkinter.messagebox import showinfo

from MineButton import MineButton


class MineField(tk.Frame):
    def __init__(self, master=None, *args, **kwargs):
        super(MineField, self).__init__(master, *args, **kwargs)
        self.row = 0
        self.column = 0
        self.size = 0
        self.mines_count = 0
        self.mines_counter = 0
        self.open_counter = 0
        self.buttons = []

    def setup(self, row: int, column: int, mines: int):
        self.mines_counter = 0
        self.open_counter = 0
        self.mines_count = mines
        if (self.row == row) and (self.column == column):
            self.game()
            return
        
        # Clear old buttons.
        for btns in self.buttons:
            for btn in btns:
                btn.destroy()

        # Refresh gui.
        self.row = row
        self.column = column
        self.size = row * column
        self.setupUi()

    def setupUi(self):
        self.buttons = []
        for i in range(self.row):
            temp = []
            for j in range(self.column):
                btn = MineButton(self, row=i, column=j)
                btn.config(command=lambda button=btn: self.click(button))
                btn.bind("<Button-3>", self.rclick)
                temp.append(btn)
            self.buttons.append(temp)

    def game(self):
        for btns in self.buttons:
            for btn in btns:
                btn.refresh()
        self.generateMines()

    def click(self, btn: MineButton):
        if str(btn["state"]) == "disabled":
            return
        btn.click()
        self.open_counter = self.open_counter + 1
        if btn.isMine:
            self.allClick()
            showinfo("Game over", "You lose!")
            return
        elif (self.open_counter + self.mines_counter) == self.row * self.column:
            showinfo("Game over", "WIN!")
            return
        elif btn.count == 0:
            for i in self.getNeightbors(btn.row, btn.column):
                self.click(i)
        
    def rclick(self, event):
        btn = event.widget
        if (self.mines_count == self.mines_counter) and (btn['text'] != MineButton.s_mine):
            return
        self.mines_counter = self.mines_counter + btn.rclick()

    def allClick(self):
        for btns in self.buttons:
            for btn in btns:
                btn.click()

    def generateMines(self):
        count = self.mines_count
        indexes = list(range(0, self.row * self.column))
        shuffle(indexes)
        indexes = indexes[:count]

        for k in indexes:
            i = k // self.column
            j = k % self.column
            self.buttons[i][j].isMine = True
            for btn in self.getNeightbors(i, j):
                btn.count = btn.count + 1

    def getNeightbors(self, row: int, column: int) -> list:
        result = []
        for i in range(row - 1, row + 2):
            for j in range(column - 1, column + 2):
                if (i < 0) or (i >= self.row):
                    continue
                if (j < 0) or (j >= self.column):
                    continue
                if (i == row) and (j == column):
                    continue
                result.append(self.buttons[i][j])
        return result

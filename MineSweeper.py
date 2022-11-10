import tkinter as tk

from MineButton import MineButton
from MineField import MineField
from MineSettings import MineSettings


class MineSweeper:
    def __init__(self):
        self.row = 10
        self.column = 10
        self.mines = 15

        self.mines_counter = 0
        self.open_counter = 0
        self.size = self.row * self.column

        self.window = tk.Tk()
        self.setupUi()

    def start(self):
        self.startGame()
        self.window.mainloop()

    def setupUi(self):
        # Setup menu.
        self.menubar = tk.Menu(self.window)
        filemenu = tk.Menu(self.menubar, tearoff=0)
        filemenu.add_command(label="New game", command=self.startGame)
        filemenu.add_command(label="Settings", command=self.startSettings)
        filemenu.add_command(label="Exit", command=self.window.destroy)
        self.menubar.add_cascade(label="Game", menu=filemenu)
        self.window.config(menu=self.menubar)

        # Setup game field.
        self.field = MineField(self.window)
        self.field.pack()

        # Setup maniwindow.
        self.window.resizable(0, 0)

    def startGame(self):
        self.mines_counter = 0
        self.open_counter = 0

        self.field.setup(row=self.row, column=self.column, mines=self.mines)
        self.field.game()

    def startSettings(self):
        winSettings = tk.Toplevel(self.window)
        frame = MineSettings(winSettings)
        frame.setup(
            row=self.row, column=self.column, mines=self.mines, func=self.updateSettings
        )
        frame.pack()

    def updateSettings(self, row: int, column: int, mines: int):
        self.row = row
        self.column = column
        self.mines = mines

        self.mines_counter = 0
        self.open_counter = 0
        self.size = self.row * self.column

        self.startGame()

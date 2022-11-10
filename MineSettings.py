import tkinter as tk

from tkinter.messagebox import showerror


class MineSettings(tk.Frame):
    def __int__(self, master=None, *args, **kwargs):
        self.row = 0
        self.col = 0
        self.count = 0
        super(MineSettings, self).__init__(master, *args, **kwargs)

    def setup(self, row: int, column: int, mines: int, func):
        self.row = row
        self.col = column
        self.count = mines
        self.func = func

        self.setupUi()

    def setupUi(self):
        label_font = ("calibre", 10, "normal")
        entry_font = ("calibre", 10, "normal")
        padx = 5
        pady = 5

        # Row input setup.
        rowlabel = tk.Label(self, text="Rows count:", font=label_font).grid(
            row=0, column=0, sticky="w", padx=padx, pady=pady
        )
        rowentry = tk.Entry(self, font=entry_font)
        rowentry.insert(0, str(self.row))
        rowentry.grid(row=0, column=1, padx=padx, pady=pady)

        # Column input setup.
        collabel = tk.Label(self, text="Columns count:", font=label_font).grid(
            row=1, column=0, sticky="w", padx=padx, pady=pady
        )
        colentry = tk.Entry(self, font=entry_font)
        colentry.insert(0, str(self.col))
        colentry.grid(row=1, column=1, padx=padx, pady=pady)

        # Mines count input setup.
        mineslabel = tk.Label(self, text="Mines count:", font=label_font).grid(
            row=2, column=0, sticky="w", padx=padx, pady=pady
        )
        minesentry = tk.Entry(self, font=entry_font)
        minesentry.insert(0, str(self.count))
        minesentry.grid(row=2, column=1, padx=padx, pady=pady)

        # Result saver.
        savebutton = tk.Button(
            self,
            text="Save",
            command=lambda: self.setupSettings(rowentry, colentry, minesentry),
        )
        savebutton.grid(row=3, column=1, padx=padx, pady=pady)

    def setupSettings(self, row: tk.Entry, col: tk.Entry, mines: tk.Entry):
        try:
            int(row.get())
            int(col.get())
            int(mines.get())
        except ValueError:
            showerror("Incorrect input", "Input correct values!")
            return

        self.row = int(row.get())
        self.col = int(col.get())
        self.count = int(mines.get())

        self.func(self.row, self.col, self.count)

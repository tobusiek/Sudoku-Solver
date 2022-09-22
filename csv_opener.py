import tkinter as tk
from tkinter import filedialog as fd
from os import curdir

class CSVSelector:
    def __init__(self) -> None:
        self.root = tk.Tk()
        self.root.title('Tkinter Open File Dialog')
        self.root.resizable(False, False)
        self.root.geometry('500x150')
        self._filename = None
        self.label = tk.Label(self.root)
        self.init_open_button()


    def init_open_button(self) -> None:
        def select_file():
            filetypes = (
                ('csv files', '*.csv'),
                ('text files', '*.txt'),
                ('All files', '*.*')
            )

            filename = fd.askopenfilename(
                initialdir=curdir,
                title='Choose a CSV file',
                filetypes=filetypes)
            
            if filename:
                self._filename = filename
            
            self.label.config(
                text=f'Chosen file:\n{self._filename}',
                wraplength=300, justify='left'
            )
            self.label.pack(expand=True)
    

        self.open_button = tk.Button(
            self.root,
            text='Choose a file',
            command=select_file
        )

        self.open_button.pack(expand=True)


    def get_filename(self) -> str:
        self.root.mainloop()
        # if self._filename:
        return self._filename

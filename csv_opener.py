import tkinter as tk
from tkinter import filedialog as fd
from os import curdir


class CSVSelector:
    def __init__(self) -> None:
        self.root = tk.Tk()
        self.root.title('Choose file for your board input')
        self.root.resizable(False, False)
        self.root.geometry('500x150')
        self._filename = None
        self.label = tk.Label(self.root)
        self.init_choosing_file()


    def init_choosing_file(self) -> None:
        def select_file():
            filetypes = (
                ('csv files', '*.csv'),
                ('text files', '*.txt'),
                ('All files', '*.*')
            )

            filename = fd.askopenfilename(
                initialdir=curdir,
                title='Choose a file',
                filetypes=filetypes)
            
            if filename:
                self._filename = filename
            
            label_text = f'Chosen file:\n{self._filename}\n\n'
            if filename:
                label_text += 'You can close this windows now.'
            else:
                label_text += 'Choose a file.'

            self.label.config(
                text=label_text,
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
        return self._filename

import tkinter as tk
from tkinter import Tk, ttk, messagebox, filedialog, simpledialog

class App():
    def __init__(self, root):
        self.root = root
        self.root.geometry('400x300')
        top_frame = ttk.Frame(root)
        ttk.Button(top_frame, text='Choose file', command=self.on_open).pack(padx=5, pady=5, side=tk.LEFT)
        ttk.Button(top_frame, text='Enter a name', command=self.on_name).pack(padx=5, pady=5, side=tk.LEFT)
        top_frame.pack()
        bottom_frame = ttk.Frame(root)
        self.result = ttk.Label(bottom_frame, text='')
        self.result.pack(padx=5, pady=5, side=tk.TOP)
        bottom_frame.pack()

    def on_open(self):
        filename = filedialog.askopenfilename(parent=self.root,
                   title='Pick a file', initialdir='.',
                   filetypes=(('Python scripts', '*.py'), ('All files', '*.*')))
        if filename is None:
            return
        self.result['text'] = filename

    def on_name(self):
        name = simpledialog.askstring(
            'Ask for name', 'What is your name?' , initialvalue='' )
        if name is None:
            return
        answer = messagebox.askyesnocancel('File', f'Confirm name: "{name}"')
        if answer is None:
            return
        self.result['text'] = f'Name "{name}" is {answer}'

def main():
    root = Tk()
    app = App(root)
    root.mainloop()


if __name__ == '__main__':
    main()

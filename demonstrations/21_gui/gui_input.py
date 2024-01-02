import tkinter as tk
from tkinter import Tk, ttk, messagebox

class App():
    def __init__(self, root):
        self.root = root
        row = ttk.Frame(root)
        ttk.Label(row, text='Number', width=10).pack(padx=5, pady=5, side=tk.LEFT)
        self.number = ttk.Entry(row, width=20)
        self.number.pack(padx=5, pady=5, side=tk.LEFT)
        row.pack()
        row = ttk.Frame(root)
        ttk.Button(row, text='Square', width=10, command=self.on_square).pack(padx=5, pady=5, side=tk.LEFT)
        self.result = ttk.Label(row, text='', width=20)
        self.result.pack(padx=5, pady=5, side=tk.LEFT)
        row.pack()
        self.number.focus()

    def on_square(self):
        try:
            self.root.config(cursor='watch')
            n = int(self.number.get())
            self.result['text'] = f'{n} squared is {n**2}'
            self.number.delete(0, tk.END)
        except ValueError:
            messagebox.showerror(title='Numeric Error', message='Invalid number.')
        finally:
            self.root.config(cursor='')

def main():
    root = Tk()
    app = App(root)
    root.mainloop()

if __name__ == '__main__':
    main()

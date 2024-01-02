import tkinter as tk
from tkinter import Tk, ttk, messagebox, font

class App():
    def __init__(self, root):
        self.root = root
        style = ttk.Style()
        style.configure('.', foreground='black', font=('Arial', 15))
        style.configure('TButton', relief='flat', font=('Arial', 15, font.ITALIC))
        style.configure('Blue.TLabel', foreground='steel blue')
        frame = ttk.Frame(root)
        ttk.Label(frame, text='Number').grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        self.number = ttk.Entry(frame)
        self.number.grid(row=0, column=1, padx=5, pady=5)
        ttk.Button(frame, text='Square', width=10, command=self.on_square) \
            .grid(row=0, column=2, padx=5, pady=5, sticky=tk.W)
        self.result = ttk.Label(frame, text='', width=20, style='Blue.TLabel')
        self.result.grid(row=1, column=0, columnspan=3, padx=5, pady=5)
        frame.pack()
        self.number.focus()

    def on_square(self):
        try:
            self.root.config(cursor='watch')
            n = int(self.number.get())
            self.result['text'] = f'{n} squared is {n ** 2}'
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

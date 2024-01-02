import tkinter as tk
from tkinter import Tk, ttk, messagebox

class App():
    def __init__(self, root):
        self.root = root
        frame = ttk.Frame(root)
        ttk.Label(frame, text='Hello World').pack(padx=5, pady=5)
        ttk.Button(frame, text='Click Me', width=10, command=self.on_click).pack(padx=5, pady=5)
        ttk.Button(frame, text='Quit', width=10, command=root.quit).pack(padx=5, pady=5)
        frame.pack()

    def on_click(self):
        messagebox.showinfo(title='Clicked', message='Button click')

def main():
    root = Tk()
    app = App(root)
    root.mainloop()

if __name__ == '__main__':
    main()

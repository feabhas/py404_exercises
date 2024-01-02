from tkinter import Tk, ttk

class App():
    def __init__(self, root):
        self.root = root
        ttk.Label(root, text='Hello World').pack()

root = Tk()
app = App(root)
root.mainloop()

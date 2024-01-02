from tkinter import Tk
from tkinter import ttk

# simple approach to avoid

app = Tk()
ttk.Label(app, text='Hello World').pack()
app.mainloop()

# various OO approches

class App():
    def __init__(self, root):
        self.root = root
        ttk.Label(root, text='Hello World').pack()

root = Tk()
app = App(root)
root.mainloop()


class Window(Tk):
    def __init__(self):
        super().__init__()
        ttk.Label(self, text='Hello World').pack()

app = Window()
app.mainloop()


from tkinter import Tk, ttk, Frame

class FrameApp(Frame):
    def __init__(self, root):
        super().__init__(master=root)
        self.root = root
        ttk.Label(self, text='Hello World').pack()
        self.pack()

root = Tk()
app = FrameApp(root)
root.mainloop()

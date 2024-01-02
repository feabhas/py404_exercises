from tkinter import Tk, ttk, messagebox, font

class App():
    def __init__(self, root):
        self.root = root
        ttk.Label(root, text='Text:').grid(row=0, column=0, padx=5, pady=5)
        self.input = ttk.Entry(root, width=40)
        self.input.grid(row=0, column=1, columnspan=2, padx=5)
        ttk.Button(root, text='Upper', command=self.on_upper).grid(row=1, column=1, pady=5)
        ttk.Button(root, text='Lower', command=self.on_lower).grid(row=1, column=2)
        self.output = ttk.Label(root, text='')
        self.output.grid(row=2, column=1, columnspan=2, pady=5)

    def on_upper(self):
        self.output.config(text=self.input.get().upper())

    def on_lower(self):
        self.output.config(text=self.input.get().lower())


root = Tk()
app = App(root)
root.mainloop()


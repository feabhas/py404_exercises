import tkinter as tk
from tkinter import Tk, ttk, messagebox
import threading as thr
from queue import Queue
import time

MESSAGE_EVENT = '<<message>>'

class App():
    def __init__(self, root):
        self.root = root
        self.queue = Queue()
        ttk.Label(root, text='Count down from:').grid(row=0, column=0, padx=5, pady=5)
        self.counter = ttk.Entry(root, width=40)
        self.counter.insert(tk.END, '5')
        self.counter.grid(row=0, column=1, padx=5)
        ttk.Button(root, text='Start', command=self.on_click).grid(row=0, column=2, padx=5, pady=5)
        self.message = ttk.Label(root, text=' ')
        self.message.grid(row=1, column=0, columnspan=3, padx=5, pady=5)
        self.root.bind(MESSAGE_EVENT, self.on_message)

    def on_click(self):
        try:
            thread = thr.Thread(target=self.countdown, args=(int(self.counter.get()),))
            thread.daemon = True
            thread.start()
        except Exception as ex:
            messagebox.showerror(message=ex)

    def countdown(self, counter):
        self.root.event_generate(MESSAGE_EVENT, when='tail', state=counter)
        while counter > 0:
            counter -= 1
            time.sleep(1)
            self.root.event_generate(MESSAGE_EVENT, when='tail', state=counter)

    def on_message(self, event):
        step = event.state
        print(step)
        self.message['text'] = str(step) if step else 'zero'

root = Tk()
app = App(root)
root.mainloop()

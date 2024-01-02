from tkinter import Tk, ttk, messagebox
import threading as thr
from queue import Queue
import time

POLL=200

class App():
    def __init__(self, root):
        self.root = root
        self.queue = Queue()
        ttk.Label(root, text='Name:').grid(row=0, column=0, padx=5, pady=5)
        self.name = ttk.Entry(root, width=40)
        self.name.grid(row=0, column=1, padx=5)
        ttk.Button(root, text='Greet slowly', command=self.on_click).grid(row=0, column=2, padx=5, pady=5)
        self.message = ttk.Label(root, text=' ')
        self.message.grid(row=1, column=0, columnspan=3, padx=5, pady=5)

    def on_click(self):
        try:
            thread = thr.Thread(target=self.build_greeting, args=(self.name.get(),))
            thread.daemon = True
            thread.start()
            self.root.after(POLL, self.poll_queue)
        except Exception as ex:
            messagebox.showerror(message=ex)

    def build_greeting(self, name):
        time.sleep(3)
        self.queue.put('Hello '+name)

    def poll_queue(self):
        if not self.queue.empty():
            message = self.queue.get()
            self.message['text'] = message
        else:
            self.message['text'] = 'Polling at {:.3f}'.format(time.time())
            self.root.after(POLL, self.poll_queue)


root = Tk()
app = App(root)
root.mainloop()

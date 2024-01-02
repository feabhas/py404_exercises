import tkinter as tk
from tkinter import Tk, ttk, messagebox, filedialog
from io import StringIO
import re

class App():
    def __init__(self, root):
        self.root = root
        root.title('Regexp Search App')
        root.geometry('648x400')
        ttk.Style().configure('.', sticky=(tk.N, tk.W))
        ttk.Style().configure('TText', background='white')

        upper_frame = ttk.Frame(root)
        ttk.Label(upper_frame, text='Patern:').pack(side=tk.LEFT, padx=5)

        self.pattern = ttk.Entry(upper_frame, width=40)
        self.pattern.pack(side=tk.LEFT, padx=5)

        ttk.Button(upper_frame, text='Load File', command=self.on_open).pack(side=tk.LEFT, padx=5)
        self.copy_button = ttk.Button(upper_frame, text='Copy to Clipboard', state=tk.DISABLED, command=self.on_copy)
        self.copy_button.pack(side=tk.LEFT, padx=5)
        upper_frame.pack(anchor=tk.W, padx=10, pady=10)

        lower_frame = ttk.Frame(root)
        scrollbar = ttk.Scrollbar(lower_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.text = tk.Text(lower_frame, wrap=tk.WORD, yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.text.yview)
        self.text.pack(fill=tk.BOTH, expand=True)
        lower_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    def on_open(self):
        try:
            dlg = filedialog.Open(self.root, filetypes=[('All files', '*')])
            filename = dlg.show()
            if not filename:
                return

            self.text.config(cursor='watch')
            self.results = self.do_search(filename, self.pattern.get())
            self.text.delete(1.0, tk.END)
            self.text.insert(tk.END, self.results)
            self.copy_button['state'] = tk.NORMAL if self.results else tk.DISABLED
        except Exception as ex:
            messagebox.showerror(message=ex)
        finally:
            self.text.config(cursor='')

    def do_search(self, filename, pattern):
        pattern = re.compile(pattern, re.IGNORECASE)
        with StringIO() as out:
            with open(filename) as fp:
                for line in fp:
                    if pattern.search(line):
                        out.write(line)
            return out.getvalue()

    def on_copy(self):
        self.root.clipboard_clear()
        self.root.clipboard_append(self.results)

def main():
    root = Tk()
    app = App(root)
    root.mainloop()

if __name__ == '__main__':
    main()

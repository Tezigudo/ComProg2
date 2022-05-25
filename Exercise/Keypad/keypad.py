import tkinter as tk
from tkinter import ttk


class Keypad(ttk.Frame):

    def __init__(self, parent, keynames=[], columns=1, **kwargs):
        super().__init__(parent, **kwargs)

        # keynames and columns
        self.keynames = keynames
        self.init_components(columns)

    def init_components(self, columns):
        """Create a stretchable keypad of keys using the keynames list,
        starting with the first keynames elements at the top of keypad.
        Use as many rows as required by the keynames.
        """

        for count, key in enumerate(self.keynames):
            button = (tk.Button(self, text=key,
                      command=lambda arg=key: print(arg)))
            button.grid(row=count // columns, column=count % columns,
                        sticky=tk.NSEW, padx=1, pady=1)

        rows, cols = self.grid_size()
        for row in range(rows):
            self.rowconfigure(row, weight=1)

        for col in range(cols):
            self.columnconfigure(col, weight=1)

    def bind(self, sequence=None, func=None, add=None):
        """Bind to this widget at event SEQUENCE a call to function FUNC.
        An additional boolean parameter ADD specifies whether FUNC will be
        called additionally to the other bound function or whether it will
        replace the previous function. See bind for the return value.
        """
        super().bind(sequence, func, add)
        for child in self.winfo_children():
            child.bind(sequence, func, add)


def load_key(event):
    """Print the key pressed in the console."""
    keyname = event.widget["text"]
    labels.set(labels.get() + keyname)


def calculate(*event):
    """Print the key pressed in the console."""
    try:
        labels.set(str(eval(labels.get())))
    except (SyntaxError, ZeroDivisionError):
        labels.set("Error")
        label.config(fg='red')


if __name__ == '__main__':
    keys = list('789456123 0.')  # = ['7','8','9',...]
    operator = ['+', '-', '*', '/']

    root = tk.Tk()
    root.title("Keypad Demo")
    keypad = Keypad(root, keynames=keys, columns=3)
    operpad = Keypad(root, keynames=operator, columns=1)
    calc = tk.Button(root, text="=", command=calculate)
    calc.bind('<Button-1>', calculate)

    labels = tk.StringVar()
    label = tk.Label(root, textvariable=labels, font={
                     'Menlo', 20}, bg='#011627')
    label.config(fg='#39FF14')

    options = {'padx': 1, 'pady': 1, 'sticky': tk.NSEW}

    label.grid(row=0, column=0, columnspan=3, **options)
    keypad.grid(row=1, column=0, **options)
    operpad.grid(row=1, column=1, **options)
    calc.grid(row=1, column=2, **options)
    root.columnconfigure(0, weight=3)
    root.columnconfigure(1, weight=1)

    keypad.bind('<Button-1>', load_key)
    operpad.bind('<Button-1>', load_key)

    root.mainloop()

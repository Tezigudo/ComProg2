import tkinter as tk
from tkinter import Label, ttk
from stopwatch import Stopwatch


# class StopwatchUI(tk.Tk):
#     """This class is graphical for the stopwatch."""

#     def __init__(self, stopwatch):
#         """Initialize"""
#         super().__init__()
#         self.stopwatch = stopwatch
#         self.initcomponents()

#     def initcomponents(self):
#         """Initialize the components."""
#         # configure someting
#         options = {'padx': 5, 'pady': 5, 'sticky': tk.NSEW}
#         font_opt = {'font': {'Menlo', 20}, 'bg': '#011627', 'fg': '#39FF14'}

#         self.title('God \'s stopwatch')
#         self.label_var = tk.StringVar()
#         self.label_var.set(f'{self.stopwatch.elapsed:.3f}')

#         # create component
#         self.label = Label(self, textvariable=self.label_var, **font_opt)
#         self.start_button = ttk.Button(
#             self, text='Start', command=self.stopwatch.start)
#         self.stop_button = ttk.Button(
#             self, text='Stop', command=self.stopwatch.stop)
#         self.reset_button = ttk.Button(
#             self, text='Reset', command=self.stopwatch.reset)

#         # weighting
#         self.columnconfigure(0, weight=2)
#         for i in range(1, 4):
#             self.columnconfigure(i, weight=1)

#         # grid
#         self.label.grid(row=0, columnspan=5, rowspan=2, **options)
#         for col, button in enumerate([self.start_button, self.stop_button, self.reset_button]):
#             button.grid(row=2, column=col, **options)

#     def update(self):
#         """Update the label with the current time."""
#         DELAY = 40
#         self.label_var.set(f'{self.stopwatch.elapsed:.3f}')
#         self.after(DELAY, self.update)

#     def run(self):
#         """Start the stopwatch."""
#         self.update()
#         self.mainloop()

class StopwatchUI(tk.Tk):

    def __init__(self, stopwatch: Stopwatch):
        super().__init__()
        self.stopwatch = stopwatch
        self.time = tk.StringVar()
        self.title('Stopwatch')
        self.init_components()

    def init_components(self):
        display = tk.Label(self, textvariable=self.time)
        display.grid(row=0, column=0, columnspan=3, padx=1, pady=1, sticky=tk.NSEW)

        start_button = tk.Button(self, text="Start", command=self.start_handler)
        start_button.grid(row=1, column=0, padx=1, pady=1, sticky=tk.NSEW)

        stop_button = tk.Button(self, text="Stop", command=self.stop_handler)
        stop_button.grid(row=1, column=2, padx=1, pady=1, sticky=tk.NSEW)

        reset_button = tk.Button(self, text="Reset", command=self.reset_handler)
        reset_button.grid(row=1, column=1, padx=1, pady=1, sticky=tk.NSEW)

        row_size, column_size = self.grid_size()
        for i in range(row_size):
            self.rowconfigure(i, weight=1)
        for i in range(column_size):
            self.columnconfigure(i, weight=1)

k = StopwatchUI(Stopwatch())
k.mainloop()

import pandas as pd
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
import matplotlib
from matplotlib.pyplot import xlabel, ylim
matplotlib.use('TkAgg')

DATASET_FILE = "rainfall.csv"


class App(tk.Frame):

    def __init__(self, parent):
        super().__init__(parent)
        self.database = pd.read_csv(DATASET_FILE)
        parent.rowconfigure(0, weight=1)
        parent.columnconfigure(0, weight=1)
        self.grid(row=0, column=0, sticky="NEWS")
        self.create_widgets()

    def create_widgets(self):
        self.slider_var = tk.IntVar()

        self.frame_panel = tk.LabelFrame(self, text="Select Year")
        self.frame_panel.grid(row=0, column=0, sticky="news")
        self.frame_panel.columnconfigure(0, weight=1)

        all_year = list(self.database.year.unique())

        self.slider_year = tk.Scale(self.frame_panel,
                                    orient=tk.HORIZONTAL, from_=min(all_year), to=max(all_year), variable=self.slider_var)
        self.slider_var.trace('w', self.plot)
        self.slider_year.grid(row=0, column=0, sticky="EW", padx=5)

        self.columnconfigure(0, weight=1)  # make slider fill the space
        self.btn_quit = tk.Button(self.frame_panel,
                                  text="Quit",
                                  command=root.destroy)
        self.btn_quit.grid(row=0, column=1, padx=5)

        self.fig = Figure()
        self.axes = self.fig.add_subplot()
        self.fig_canvas = FigureCanvasTkAgg(self.fig, master=self)
        self.fig_canvas.get_tk_widget().grid(
            row=1, column=0, sticky="NEWS", padx=5, pady=5)
        self.rowconfigure(1, weight=1)  # make plot fill the space

        self.plot(0)  # this is maybe hard code

    def plot(self, *event):
        year = self.slider_var.get()
        data = self.database[self.database.year == year]
        ylim = self.database.rainfall.max()
        self.axes.clear()
        data.plot(kind="bar", ax=self.axes, x='month', y='rainfall', ylim=(
            0, ylim), ylabel='Rainfall(mm)', xlabel='Month', title=f'Monthly Rainfall in {year}')
        self.fig_canvas.draw()


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Monthly Rainfall Comparison")
    root.geometry("800x600")
    app = App(root)
    root.mainloop()

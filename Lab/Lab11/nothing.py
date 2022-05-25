import pandas as pd
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
import tkinter.ttk as ttk
import matplotlib
matplotlib.use('TkAgg')


class App(ttk.Frame):

    def __init__(self, parent):
        super().__init__(parent)
        self.df = pd.read_csv("titanic.csv")
        parent.rowconfigure(0, weight=1)
        parent.columnconfigure(0, weight=1)
        self.grid(row=0, column=0, sticky="news")
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.columnconfigure(0, weight=1)
        self.create_widgets()

    def create_widgets(self):
        # creating a row with combobox widgets for filters
        self.frame_filter = ttk.LabelFrame(self, text="Select Filters")
        self.frame_filter.grid(row=2, column=0, sticky="NEWS")
        label1 = ttk.Label(self.frame_filter, text="Gender")
        label1.grid(row=0, column=0)
        self.cb_gender_filter = ttk.Combobox(
            self.frame_filter, state="readonly")
        self.cb_gender_filter.bind('<<ComboboxSelected>>', self.update_filters)
        self.cb_gender_filter.grid(row=1, column=0, padx=10, pady=10)

        label2 = ttk.Label(self.frame_filter, text="Passenger Class")
        label2.grid(row=0, column=1)
        self.cb_pclass_filter = ttk.Combobox(
            self.frame_filter, state="readonly")
        self.cb_pclass_filter.bind('<<ComboboxSelected>>', self.update_filters)
        self.cb_pclass_filter.grid(row=1, column=1, padx=10, pady=10)

        self.btn_quit = ttk.Button(self, text="Quit", command=root.destroy)
        self.btn_quit.grid(row=3, column=0, pady=10)
        self.btn_quit = ttk.Button(self, text="Quit", command=root.destroy)

        # create Matplotlib figure and plotting axes
        self.fig_survived = Figure()
        self.axes_survived = self.fig_survived.add_subplot()

        # create a canvas to host the figure and place it into the main window
        self.fig_canvas1 = FigureCanvasTkAgg(self.fig_survived, master=self)
        self.fig_canvas1.get_tk_widget().grid(row=0, column=0, sticky="news",
                                              padx=10, pady=10)
        self.plot_survived()

        # create Matplotlib figure and plotting axes
        self.fig_nonsurvived = Figure()
        self.axes_nonsurvived = self.fig_nonsurvived.add_subplot()

        # create a canvas to host the figure and place it into the main window
        self.fig_canvas2 = FigureCanvasTkAgg(self.fig_nonsurvived, master=self)
        self.fig_canvas2.get_tk_widget().grid(row=1, column=0, sticky="news",
                                              padx=10, pady=10)
        self.plot_nonsurvived()

    def update_filters(self, ev):
        # compute dataframe filter here
        pass

    def plot_survived(self):
        self.axes_survived.clear()
        self.fig_survived.subplots_adjust(bottom=0.25)
        df = self.df
        df[df.Survived == 1].Age.plot.hist(ax=self.axes_survived)
        self.axes_survived.set(xlabel="Age", ylabel="Count",
                               title="Survived", xlim=[0, 100])
        self.fig_canvas1.draw()

    def plot_nonsurvived(self):
        self.axes_nonsurvived.clear()
        self.fig_nonsurvived.subplots_adjust(bottom=0.25)
        df = self.df
        df[df.Survived == 0].Age.plot.hist(ax=self.axes_nonsurvived)
        self.axes_nonsurvived.set(xlabel="Age", ylabel="Count",
                                  title="Non-Survived", xlim=[0, 100])
        self.fig_canvas2.draw()


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Matplotlib Integration")
    root.geometry("600x800")
    app = App(root)
    root.mainloop()

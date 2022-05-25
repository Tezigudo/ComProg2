import tkinter as tk
from traffic_light import TrafficLight

class App(tk.Frame):

    def __init__(self, parent):
        super().__init__(parent)
        self.pack(fill=tk.BOTH, expand=1)
        self.canvas = tk.Canvas(self, borderwidth=0, highlightthickness=0)
        self.traffic_light = TrafficLight(self.canvas)
        self.canvas.pack(fill=tk.BOTH, expand=1)
        self.traffic_light.state = 'red'
        self.change_state()

    def change_state(self):
        if self.traffic_light.state == "green":
            self.traffic_light.state = "yellow"
            self.after(1000, self.change_state)
        elif self.traffic_light.state == "yellow":
            self.traffic_light.state = "red"
            self.after(3000, self.change_state)
        elif self.traffic_light.state == "red":
            self.traffic_light.state = "green"
            self.after(2000, self.change_state)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Traffic Light")
    root.geometry("250x500")
    app = App(root)
    root.mainloop()


import tkinter as tk

class TrafficLight:
    
    def __init__(self, canvas: tk.Canvas) -> None:
        self.canvas = canvas
        self.COLOR_LST = ["red", "yellow", "green"]
        self.state = None
        self.draw()

    def draw(self):
        self.rectangle_id = self.canvas.create_rectangle(30, 40, 210, 470, fill="black")
        self.light0_id = self.canvas.create_oval(60, 60, 180, 180, fill='grey', tag=['light'])
        self.light1_id = self.canvas.create_oval(60, 190, 180, 310, fill='grey', tag=['light'])
        self.light2_id = self.canvas.create_oval(60, 320, 180, 440, fill='grey', tag=['light'])
        self.light_id_tup = (self.light0_id, self.light1_id, self.light2_id)


    @property
    def state(self):
        return self.__state

    @state.setter
    def state(self, other_state):
        if other_state not in self.COLOR_LST + [None]:
            raise ValueError("Invalid state")
        self.set_color(other_state)
        self.__state = other_state

    def set_color(self, color):
        if color is None:
            self.canvas.itemconfigure('light', fill='grey')
        else:
            color_ind = self.COLOR_LST.index(color)
            light_id = self.light_id_tup[color_ind]
            prev = (color_ind - 1) % 3
            self.canvas.itemconfigure(light_id, fill=color)
            for i in range(2):
                self.canvas.itemconfigure(self.light_id_tup[prev-i], fill='grey')

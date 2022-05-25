import time
import tkinter as tk
import tkinter.ttk as ttk


class Ball:

    def __init__(self, canvas, start_pos, size, color, speed):
        self.__canvas = canvas
        self.__size = size
        self.__id = canvas.create_oval(0, 0, size, size, fill=color)
        self.__speed = speed
        self.__start_pos = start_pos
        self.__x = 0
        self.__y = 0
        self.reset()

    def reset(self):
        x, y = self.__start_pos
        self.move_to(x, y)

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @property
    def speed(self):
        return self.__speed

    @property
    def size(self):
        return self.__size

    def move_to(self, x, y):
        self.__x = x
        self.__y = y
        self.__canvas.moveto(self.__id, x - self.size / 2, y - self.size / 2)

    def update(self):
        # move the ball by 'speed' pixels to the right every time it is updated
        self.move_to(self.x + self.speed, self.y)


class App(ttk.Frame):

    def __init__(self, parent):
        super().__init__(parent)
        parent.rowconfigure(0, weight=1)
        parent.columnconfigure(0, weight=1)
        self.grid(row=0, column=0, sticky="news")
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.create_widgets()
        self.is_animating = False
        self.balls = [
            Ball(self.canvas, (0, 50), 10, "blue", 3),
            Ball(self.canvas, (0, 50), 14, "green", 2),
            Ball(self.canvas, (0, 50), 18, "red", 1),
        ]

    def create_widgets(self):
        self.canvas = tk.Canvas(self,
                                borderwidth=0,
                                highlightthickness=0, bg="yellow")
        self.canvas.grid(row=0, column=0, columnspan=3,
                         sticky="news", padx=10, pady=10)
        self.btn_start = ttk.Button(self, text="Start",
                                    command=self.toggle_animation)
        self.btn_reset = ttk.Button(self, text="Reset",
                                    command=self.reset_animation)
        self.btn_quit = ttk.Button(self, text="Quit",
                                   command=root.destroy)
        self.btn_start.grid(row=1, column=0, pady=10)
        self.btn_reset.grid(row=1, column=1, pady=10)
        self.btn_quit.grid(row=1, column=2, pady=10)

    def toggle_animation(self):
        self.is_animating = not self.is_animating
        if self.is_animating:
            self.btn_start.config(text="Stop")
            self.animate()
        else:
            self.btn_start.config(text="Start")

    def reset_animation(self):
        for ball in self.balls:
            ball.reset()

    def animate(self):
        for ball in self.balls:
            ball.update()
        if self.is_animating:
            self.after(10, self.animate)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Basic Animation")
    root.geometry("300x300")
    app = App(root)
    root.mainloop()

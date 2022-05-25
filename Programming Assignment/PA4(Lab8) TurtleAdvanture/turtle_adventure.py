"""
The turtle_adventure module maintains all classes related to the Turtle's
adventure game.
"""
import tkinter as tk
from typing import Final, Tuple, List
from turtle import RawTurtle, TurtleScreen
from gamelib import Game, GameElement
from enemies import Enemy, EnemyGenerator


class Waypoint(GameElement):
    """
    Represent the waypoint to which the player will move.
    """

    def __init__(self, game: "TurtleAdventureGame") -> None:
        super().__init__(game)
        self.__game: "TurtleAdventureGame" = game
        self.__id1: int
        self.__id2: int
        self.__active: bool = False

    def create(self) -> None:
        self.__id1 = self.canvas.create_line(0, 0, 0, 0, width=2, fill="green")
        self.__id2 = self.canvas.create_line(0, 0, 0, 0, width=2, fill="green")

    def delete(self) -> None:
        self.canvas.delete(self.__id1)
        self.canvas.delete(self.__id2)

    def update(self) -> None:
        # there is nothing to update because a waypoint is fixed
        pass

    def render(self) -> None:
        if self.is_active:
            self.canvas.itemconfigure(self.__id1, state="normal")
            self.canvas.itemconfigure(self.__id2, state="normal")
            self.canvas.tag_raise(self.__id1)
            self.canvas.tag_raise(self.__id2)
            self.canvas.coords(self.__id1, self.x-10,
                               self.y-10, self.x+10, self.y+10)
            self.canvas.coords(self.__id2, self.x-10,
                               self.y+10, self.x+10, self.y-10)
        else:
            self.canvas.itemconfigure(self.__id1, state="hidden")
            self.canvas.itemconfigure(self.__id2, state="hidden")

    def activate(self, x: float, y: float) -> None:
        """
        Activate this waypoint with the specified location.
        """
        self.__active = True
        self.x = x
        self.y = y

    def deactivate(self) -> None:
        """
        Mark this waypoint as inactive.
        """
        self.__active = False

    @property
    def is_active(self) -> bool:
        """
        Get the flag indicating whether this waypoint is active.
        """
        return self.__active


class Home(GameElement):
    """
    Represent the player's home.
    """

    def __init__(self, game: "TurtleAdventureGame", pos: Tuple[int, int], size: int):
        super().__init__(game)
        self.__game: "TurtleAdventureGame" = game
        self.__id: int
        self.__size: int = size
        x, y = pos
        self.x = x
        self.y = y

    @property
    def size(self) -> int:
        return self.__size

    @size.setter
    def size(self, val: int) -> None:
        self.__size = val

    def create(self) -> None:
        self.__id = self.canvas.create_rectangle(
            0, 0, 0, 0, outline="brown", width=2)

    def delete(self) -> None:
        self.canvas.delete(self.__id)

    def update(self) -> None:
        # there is nothing to update, unless home is allowed to moved
        pass

    def render(self) -> None:
        self.canvas.coords(self.__id,
                           self.x - self.size/2,
                           self.y - self.size/2,
                           self.x + self.size/2,
                           self.y + self.size/2)

    def contains(self, x: float, y: float) -> bool:
        """
        Check whether home contains the point (x, y).
        """
        x1, x2 = self.x-self.size/2, self.x+self.size/2
        y1, y2 = self.y-self.size/2, self.y+self.size/2
        return x1 <= x <= x2 and y1 <= y <= y2


class Player(GameElement):
    """
    Represent the main player, implemented using Python's turtle.
    """

    def __init__(self,
                 game: "TurtleAdventureGame",
                 turtle: RawTurtle,
                 waypoint: Waypoint,
                 home: Home,
                 speed: float = 5) -> None:
        super().__init__(game)
        # self.__game: "TurtleAdventureGame" = game
        self.__waypoint: Waypoint = waypoint
        self.__home: Home = home
        self.__speed: float = speed
        self.__turtle: RawTurtle = turtle

    def create(self) -> None:
        turtle = RawTurtle(self.canvas)
        turtle.getscreen().tracer(False)  # disable turtle's built-in animation
        turtle.shape("turtle")
        turtle.color("#15F4EE")
        turtle.penup()
        turtle.screen.bgcolor('#011627')

        self.__turtle=turtle

    @ property
    def speed(self) -> float:
        """
        Give the player's current speed.
        """
        return self.__speed

    @ speed.setter
    def speed(self, val: float) -> None:
        self.__speed=val

    def delete(self) -> None:
        pass

    def update(self) -> None:
        # check if player has arrived home
        if self.__home.contains(self.x, self.y):
            self.game.game_over_win()
        waypoint=self.__waypoint
        turtle=self.__turtle
        if waypoint.is_active:
            turtle.setheading(turtle.towards(waypoint.x, waypoint.y))
            turtle.forward(self.speed)
            if turtle.distance(waypoint.x, waypoint.y) < self.speed:
                waypoint.deactivate()

    def render(self) -> None:
        self.__turtle.goto(self.x, self.y)
        self.__turtle.getscreen().update()

    # override original property x's getter/setter to use turtle's methods
    # instead
    @ property
    def x(self) -> float:
        return self.__turtle.xcor()

    @ x.setter
    def x(self, val: float) -> None:
        self.__turtle.setx(val)

    # override original property y's getter/setter to use turtle's methods
    # instead
    @ property
    def y(self) -> float:
        return self.__turtle.ycor()

    @ y.setter
    def y(self, val: float) -> None:
        self.__turtle.sety(val)


class TurtleAdventureGame(Game):
    """
    The main class for Turtle's Adventure.
    """

    def __init__(self, parent, screen_width: int, screen_height: int, level: int=1) -> None:
        self.level: int=level
        self.screen_width: int=screen_width
        self.screen_height: int=screen_height
        self.waypoint: Waypoint
        self.player: Player
        self.home: Home
        self.enemies: List[Enemy]
        self.enemy_generator: EnemyGenerator
        super().__init__(parent)

    def init_game(self) -> None:
        self.canvas.config(width=self.screen_width,
                           height=self.screen_height, bg='#011627')
        turtle=RawTurtle(self.canvas)
        # set turtle screen's origin to the top-left corner
        turtle.screen.setworldcoordinates(
            0, self.screen_height-1, self.screen_width-1, 0)

        self.waypoint=Waypoint(self)
        self.add_element(self.waypoint)
        self.home=Home(self, (self.screen_width-100,
                         self.screen_height//2), 20)
        self.add_element(self.home)
        self.player=Player(self, turtle, self.waypoint, self.home)
        self.add_element(self.player)
        self.canvas.bind(
            "<Button-1>", lambda e: self.waypoint.activate(e.x, e.y))

        self.enemies=[]
        self.enemy_generator=EnemyGenerator(self, level=self.level)

        self.player.x=50
        self.player.y=self.screen_height//2

    def add_enemy(self, enemy: Enemy) -> None:
        self.enemies.append(enemy)
        self.add_element(enemy)

    def game_over_win(self) -> None:
        self.stop()
        font=("Menlo", 36, "bold")
        self.canvas.create_text(
            self.screen_width/2, self.screen_height/2, text="You Win", font=font, fill="#7FFF00")

    def game_over_lose(self) -> None:
        self.stop()
        font=("Menlo", 36, "bold")
        self.canvas.create_text(
            self.screen_width/2, self.screen_height/2, text="You Lose", font=font, fill="#F21A1D")

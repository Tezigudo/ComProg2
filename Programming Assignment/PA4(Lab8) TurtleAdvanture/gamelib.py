"""
The gamelib module defines abstract classes necessary for implementing simple
games based on tkinter's canvas.
"""
import tkinter as tk
from abc import ABC, abstractmethod


class GameElement(ABC):
    """
    An abstract class to be implemented to represent all kinds of elements to
    be displayed on the game's screen
    """

    def __init__(self, game: "Game"):
        self.__game: "Game" = game
        self.__x: float = 0
        self.__y: float = 0

    @property
    def x(self) -> float:
        """
        Get or set the x coordinate of the element
        """
        return self.__x

    @x.setter
    def x(self, val: float) -> None:
        self.__x = val

    @property
    def y(self) -> float:
        """
        Get or set the y coordinate of the element
        """
        return self.__y

    @y.setter
    def y(self, val: float) -> None:
        self.__y = val

    @property
    def canvas(self) -> tk.Canvas:
        return self.__game.canvas

    @abstractmethod
    def create(self) -> None:
        """
        Create a game object, e.g., canvas item, representing this element
        """

    @abstractmethod
    def update(self) -> None:
        """
        Update internal states of this element
        """

    @abstractmethod
    def render(self) -> None:
        """
        Render the corresponding game object with the current item properties
        """

    @abstractmethod
    def delete(self) -> None:
        """
        Delete the corresponding game object, e.g., canvas item
        """

    @property
    def game(self):
        return self.__game

    @property
    def coordinate(self):
        return self.x, self.y


class Game(tk.Frame, ABC):
    """
    An abstract class to be implemented with a concrete game class that relies
    on update/render loop
    """

    def __init__(self, parent, update_delay=33):
        super().__init__(parent)
        self.__canvas = tk.Canvas(self, bg='#011627')
        self.__canvas.pack(expand=True, fill="both")
        self.pack(expand=True, fill="both")
        self.__game_elements = []
        self.__update_delay = update_delay
        self.__started = False
        self.init_game()

    @abstractmethod
    def init_game(self) -> None:
        """
        Create game elements and initialize other game-specific attributes
        """

    def add_element(self, element: GameElement) -> None:
        """
        Add a GameElement object to the game
        """
        element.create()
        self.__game_elements.append(element)

    def delete_element(self, element: GameElement) -> None:
        """
        Remove a GameElement object to the game
        """
        element.delete()
        self.__game_elements.remove(element)

    @property
    def canvas(self) -> tk.Canvas:
        """
        Get the canvas object of the game application
        """
        return self.__canvas

    @property
    def is_started(self) -> bool:
        """
        Get the flag indicating whether the game has started and is running
        """
        return self.__started

    def start(self) -> None:
        """
        Start the game
        """
        if not self.__started:
            self.__started = True
            self.animate()

    def stop(self) -> None:
        """
        Stop the game
        """
        self.__started = False

    def animate(self):
        """
        Update and render all game's elements
        """
        for element in self.__game_elements:
            element.update()
            element.render()
        if self.__started:
            self.after(self.__update_delay, self.animate)

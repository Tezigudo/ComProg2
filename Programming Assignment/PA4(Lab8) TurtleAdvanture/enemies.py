"""
The enemies module is responsible for defining enemy classes with various
behaviours.  It also contains logic to make enemies show up in the game at
certain points in time.
"""

import random
from math import floor
from time import perf_counter
from typing import Type, Union

import turtle_adventure
from gamelib import GameElement


class Enemy(GameElement):
    """
    Define an enemy for the Turtle's adventure game with specific behaviors
    """

    SPEED: float = 4  # class attribute speed to implement each enemy type speed
    TAG: str

    def __init__(self, game: "turtle_adventure.TurtleAdventureGame", size: int, color: str) -> None:
        """Initialize"""
        super().__init__(game)
        self.size = size
        self.color = color
        self.__origincolor = color
        self.__X_STATE = self.state_move_right
        self.__Y_STATE = self.state_move_up
        self.__id: int
        self.init_tag()
        self.__counter = 0
        # self.change_color()

    @property
    def X_STATE(self):
        return self.__X_STATE

    @X_STATE.setter
    def X_STATE(self, func):
        self.__X_STATE = func

    @property
    def Y_STATE(self):
        return self.__Y_STATE

    @Y_STATE.setter
    def Y_STATE(self, func):
        self.__Y_STATE = func

    @classmethod
    @property
    def speed(cls) -> float:
        return cls.SPEED

    @property
    def id(self) -> int:
        return self.__id

    @classmethod
    @property
    def tag(cls):
        return cls.TAG

    @classmethod
    def init_tag(cls):
        cls.TAG = cls.__name__

    @property
    def origin_color(self) -> str:
        return self.__origincolor

    @origin_color.setter
    def origin_color(self, color) -> None:
        if not isinstance(color, str):
            raise TypeError("color must be a string")
        self.__origincolor = color

    @property
    def counter(self):
        return self.__counter

    @counter.setter
    def counter(self, value):
        self.__counter = value

    @property
    def trasforming_state(self):
        if self.counter % 166 < 130:
            return 'normal'
        if self.counter % 166 < 165:
            return 'transforming'
        if self.counter % 166 == 165:
            return 'transformed'

    def spawn(self) -> None:
        """
        Spawn an enemy at random position
        """
        while True:
            self.x = random.randrange(self.game.winfo_width())
            self.y = random.randrange(self.game.winfo_height())
            if self.valid_spawn():
                break

    def create(self) -> None:
        """creating enemy to a canvas"""

        self.__id = self.canvas.create_oval(
            0, 0, 0, 0, fill=self.color, outline='#011627', tag=[self.tag])

    def update(self) -> None:
        """update a motion and graphic"""
        if self.is_collaspe():
            self.game.game_over_lose()
        self.motion()

    def render(self) -> None:
        """render a enemy"""
        self.canvas.coords(self.id, self.x - self.size/2, self.y -
                           self.size/2, self.x + self.size/2, self.y + self.size/2)

    def delete(self) -> None:
        """delete an element of a cancas"""
        self.canvas.delete(self.id)

    def motion(self) -> None:
        """implement a motion of each enemy"""
        self.__counter += 1
        self.X_STATE()
        self.Y_STATE()

    def move_to(self, x, y) -> None:
        """move an enemy"""
        self.x = x
        self.y = y

    def state_nothing(self) -> None:
        """This state do nothing"""

    def state_move_right(self) -> None:
        """state to move right"""
        self.move_to(self.x + self.speed, self.y)
        if self.x > self.game.winfo_width():
            self.X_STATE = self.state_move_left

    def state_move_left(self) -> None:
        """state to move left"""
        self.move_to(self.x - self.speed, self.y)
        if self.x < 0:
            self.X_STATE = self.state_move_right

    def state_move_up(self) -> None:
        """state to move up"""
        self.move_to(self.x, self.y + self.speed)
        if self.y > self.game.winfo_height():
            self.Y_STATE = self.state_move_down

    def state_move_down(self) -> None:
        """state to move down"""
        self.move_to(self.x, self.y - self.speed)
        if self.y < 0:
            self.Y_STATE = self.state_move_up

    def is_collaspe(self) -> bool:
        """
        Check whether Enemy collaspe with player
        """
        player_x, player_y = self.game.player.coordinate
        x1, x2 = self.x-self.size/2, self.x+self.size/2
        y1, y2 = self.y-self.size/2, self.y+self.size/2
        return x1 <= player_x <= x2 and y1 <= player_y <= y2

    def distance(self, x, y) -> float:
        """
        Calculate the distance between the enemy and the point (x, y)
        """
        return ((self.x - x)**2 + (self.y - y)**2)**0.5

    def valid_spawn(self) -> bool:
        """check whether any enemy can spawn or not
            enemy must spawn near home or player
        """
        element_list = [self.game.player, self.game.home]
        return all(self.distance(*element.coordinate) > self.size + 15 for element in element_list)

    def change_color(self):
        """change color of enemy"""
        if self.game.is_started:
            # if state is transforming colot will randomize
            if self.trasforming_state == 'transforming':
                RAINBOW_COLOR_LIST = ['#FCF340', '#0310EA', '#7FFF00', '#FB33DB',
                                      '#A0EDFF', '#79FFFE', '#01FFFF', '#9D72FF',
                                      '#FF8B8B', '#FF0000', '#00207F', '#FFDEF3',
                                      '#13CA91', '#FDF200', '#00FECA', '#FF2281',
                                      '#08F7FE', '#CEFF03', '#FF073A', '#CB06FF']
                DELAY = 500
                # change color of enemy
                self.color = random.choice(RAINBOW_COLOR_LIST)
            # if state is normal color must be original number
            elif self.trasforming_state in ('normal', 'transformed'):
                self.color = self.__origincolor

            self.game.canvas.itemconfigure(self.tag, fill=self.color)
            self.game.after(DELAY, self.change_color)

class RandomWalkEnemy(Enemy):
    """
    An enemy that moves randomly in the game
    """

    SPEED = 6

    def motion(self) -> None:
        """randomize a motion of an enemy of x and y"""
        state_x_list = [self.state_move_right,
                        self.state_move_left, self.state_nothing]
        state_y_list = [self.state_move_up,
                        self.state_move_down, self.state_nothing]
        self.X_STATE = random.choice(state_x_list)
        self.Y_STATE = random.choice(state_y_list)
        super().motion()


class ChasingEnemy(Enemy):
    """
    An enemy that chases the player
    """

    SPEED = 1

    def motion(self) -> None:
        """follow an player"""
        player_x, player_y = self.game.player.coordinate
        # x state
        if self.x < player_x:
            self.X_STATE = self.state_move_right
        else:
            self.X_STATE = self.state_move_left
        # y state
        if self.y < player_y:
            self.Y_STATE = self.state_move_up
        else:
            self.Y_STATE = self.state_move_down
        super().motion()


class FencingEnemy(Enemy):
    """
    An enemy that walk around the home in square pattern
    """

    SPEED = 2.5
    HOME_OFFSET = 20

    def __init__(self, game: "turtle_adventure.TurtleAdventureGame", size: int, color: str) -> None:
        super().__init__(game, size, color)
        # create a border
        self.__LEFT_BORDER: float = self.game.home.x - \
            self.game.home.size/2 - self.HOME_OFFSET
        self.__RIGHT_BORDER: float = self.game.home.x + \
            self.game.home.size/2 + self.HOME_OFFSET
        self.__TOP_BORDER: float = self.game.home.y + \
            self.game.home.size/2 + self.HOME_OFFSET
        self.__BOTTOM_BORDER: float = self.game.home.y - \
            self.game.home.size/2 - self.HOME_OFFSET

    def spawn(self) -> None:
        """spawn an enemy at anywhere in square around the home"""
        def left_spawn() -> None:
            """spawn an enemy at left side of the home"""
            self.x = self.__LEFT_BORDER
            self.y = random.randint(self.__BOTTOM_BORDER, self.__TOP_BORDER)

        def right_spawn() -> None:
            """spawn an enemy at right side of the home"""
            self.x = self.__RIGHT_BORDER
            self.y = random.randint(self.__BOTTOM_BORDER, self.__TOP_BORDER)

        def top_spawwn() -> None:
            """spawn an enemy at top side of the home"""
            self.x = random.randint(self.__LEFT_BORDER, self.__RIGHT_BORDER)
            self.y = self.__TOP_BORDER

        def bottom_spawn() -> None:
            """spawn an enemy at bottom side of the home"""
            self.x = random.randint(self.__LEFT_BORDER, self.__RIGHT_BORDER)
            self.y = self.__BOTTOM_BORDER

        spawn_list = [left_spawn, right_spawn, top_spawwn, bottom_spawn]

        spawner = random.choice(spawn_list)
        spawner()

    def state_move_right(self) -> None:
        """state to move right which change border to left border of home"""
        self.move_to(self.x + self.speed, self.y)
        if self.x > self.__RIGHT_BORDER:
            self.X_STATE = self.state_nothing
            self.Y_STATE = self.state_move_up

    def state_move_left(self) -> None:
        """state to move left which change border to right border of home"""
        self.move_to(self.x - self.speed, self.y)
        if self.x < self.__LEFT_BORDER:
            self.X_STATE = self.state_nothing
            self.Y_STATE = self.state_move_down

    def state_move_up(self) -> None:
        """state to move up which change border to bottom border of home"""
        self.move_to(self.x, self.y + self.speed)
        if self.y > self.__TOP_BORDER:
            self.Y_STATE = self.state_nothing
            self.X_STATE = self.state_move_left

    def state_move_down(self) -> None:
        """state to move down which change border to top border of home"""
        self.move_to(self.x, self.y - self.speed)
        if self.y < self.__BOTTOM_BORDER:
            self.Y_STATE = self.state_nothing
            self.X_STATE = self.state_move_right

    def valid_spawn(self) -> None:
        # This enemy does not require any validation
        pass


class TransformEnemy(Enemy):
    """This Enemy can transform into other Enemy evey 3 seconds"""

    SPEED = 10
    __now_enemy = None  # now transforming enemy
    __borntime: float = perf_counter()

    def __init__(self, game: "turtle_adventure.TurtleAdventureGame", size: int, color: str) -> None:
        """Initialize Transformation enemy with an enemy dict"""
        super().__init__(game, size, color)
        self.enemy_dict = {RandomWalkEnemy: RandomWalkEnemy(game, size=20, color='red'),
                           ChasingEnemy: ChasingEnemy(game, size=15, color='green'),
                           FencingEnemy: FencingEnemy(game, size=10, color='brown'),
                           None: None}

    def init_enemy(self):
        """initialize other enemy state to hidden"""
        for enemy in self.enemy_dict.values():
            if enemy is not None:
                self.canvas.itemconfigure(enemy.id, state='hidden')

    @classmethod
    def get_enemy(cls) -> Enemy:
        """get enemy to transform"""
        return cls.__now_enemy

    @classmethod
    def set_enemy(cls, enemy: Union[Enemy, Type[None]]) -> None:
        """set enemy to transform"""
        cls.__now_enemy = enemy

    @property
    def now(self) -> Enemy:
        """get the now enemy"""
        return self.enemy_dict[self.__now_enemy]

    @classmethod
    @property
    def elasped_time(cls) -> float:
        """get elasped time since init the class"""
        return perf_counter() - cls.__borntime

    def create(self) -> None:
        """create an enemy in the game of all transfroming and transformed enemy"""
        for enemy in self.enemy_dict.values():
            if enemy is not None:
                enemy.create()
            else:
                super().create()
        self.init_enemy()

    @property
    def id(self) -> int:
        """get the id of now enemy"""
        enemy = self.get_enemy()
        return super().id if enemy is None else self.enemy_dict[enemy].id

    def spawn(self) -> None:
        """spawn an enemy in the game of all transfroming and transformed enemy"""
        for enemy_type, enemy in self.enemy_dict.items():
            if enemy_type is not None:
                enemy.spawn()
            else:
                super().spawn()

    def delete(self) -> None:
        """delete an enemy in the game of all transfroming and transformed enemy"""
        for enemy_type, enemy in self.enemy_dict.items():
            if enemy_type is not None:
                enemy.delete()
            else:
                super().delete()

    def render(self) -> None:
        """render an enemy in the game of all transfroming and transformed enemy"""
        if self.get_enemy() is None:
            super().render()
        else:
            self.now.render()

    def move_to(self, x: float, y: float) -> None:
        """move an enemy in the game of all transfroming and transformed enemy"""
        for enemy in self.enemy_dict.values():
            if enemy is None:
                super().move_to(x, y)
            else:
                enemy.move_to(x, y)

    def motion(self) -> None:
        """motion an enemy in the game of all transfroming and transformed enemy"""
        if not self.get_enemy():
            super().motion()
        else:
            self.now.motion()

        self.change_color()

        if self.trasforming_state == 'transformed':
            self.transform()

    def transform(self) -> None:
        """transform all enemy every 5 second"""
        # BUG: enemmy is not transform
        # TODO: fix the bug that enemy is not transform
        # hide a transforming enemy
        self.canvas.itemconfigure(self.id, state='hidden')
        self.set_enemy(random.choice(list(self.enemy_dict.keys())))

        # set a current transforming to visible state
        self.canvas.itemconfigure(self.id, state='normal')

    def change_color(self) -> None:
        """change color of all enemy every 3 second"""
        enemy = self.get_enemy()
        if enemy is None:
            super().change_color()
        else:
            self.enemy_dict[enemy].change_color()


class EnemyGenerator:
    """
    An EnemyGenerator instance is responsible for creating enemies of various
    kinds and scheduling them to appear at certain points in time.
    """

    def __init__(self, game: "turtle_adventure.TurtleAdventureGame", level: int) -> None:
        """Initialize the game with game lecel and counter its time"""
        self.__game: "turtle_adventure.TurtleAdventureGame" = game
        self.__level: int = level
        self.__start = perf_counter()
        self.update()
        # self.create_random_walk_enemy()
        # self.create_chasing_enemy()
        # self.create_transform_enemy()

    def is_started(self):
        """check whether the game is started"""
        return self.__game.is_started or self.elasped < 5

    @property
    def level(self) -> int:
        """get current level of game"""
        return self.__level

    @property
    def elasped(self) -> float:
        """get elasped time  since init the class"""
        return perf_counter() - self.__start

    def create_random_walk_enemy(self) -> None:
        """
        Create a random walk enemy
        """
        enemy = RandomWalkEnemy(self.__game, 20, '#FFFF66')
        self.__game.add_enemy(enemy)
        enemy.spawn()
        # schedule the enemy to spawn again
        if self.is_started():
            self.__game.after(150*(floor(self.elasped % 5)+1),
                              self.create_random_walk_enemy)

    def create_chasing_enemy(self) -> None:
        """
        Create a chasing enemy
        """
        enemy = ChasingEnemy(self.__game, 15, '#ff8800')
        self.__game.add_enemy(enemy)
        enemy.spawn()
        if self.is_started():
            self.__game.after(200 * (floor(self.elasped %
                              5) + 1), self.create_chasing_enemy)

    def create_fencing_enemy(self) -> None:
        """
        Create a fancing enemy
        """
        enemy = FencingEnemy(self.__game, 15, 'brown')
        self.__game.add_enemy(enemy)
        enemy.spawn()
        # schedule the enemy to spawn again
        if self.is_started():
            self.__game.after(800 * (floor(self.elasped %
                              5) + 1), self.create_fencing_enemy)

    def create_transform_enemy(self) -> None:
        """
        Create a transform enemy
        """
        enemy = TransformEnemy(self.__game, 20, '#39FF14')
        self.__game.add_enemy(enemy)
        enemy.spawn()
        # schedule the enemy to spawn again
        if self.is_started():
            self.__game.after(3000, self.create_transform_enemy)

    def increase_level(self) -> None:
        """increase level and illustrate level on the screen"""
        self.__level += 1
        print('level increased!')
        print(f'level {self.level}')

    def create_enemy(self) -> None:
        """generate an enemy of each level"""
        if self.level == 1:
            self.create_random_walk_enemy()
        elif self.level == 2:
            self.create_chasing_enemy()
        elif self.level == 3:
            self.create_fencing_enemy()
        elif self.level == 4:
            self.create_transform_enemy()
        else:

            func_list = [self.create_random_walk_enemy, self.create_chasing_enemy,
                         self.create_fencing_enemy, self.create_transform_enemy]
            random.choice(func_list)()  # spawn an randomed enemy

    def update(self) -> None:
        """update the level of game"""
        if not floor(self.elasped) % 3:
            self.increase_level()
            self.create_enemy()
        self.__game.after(1000, self.update)

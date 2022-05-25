""" This is food module that contain Problem1 and Problem2 for quiz xD"""

from typing import Union, List


# Problem1
class Food:
    """A portion of food with a name, weight (grams),
    calories (the energy value), and carbohydrates (grams).
    """

    def __init__(self, name: str, weight: Union[int, float],
                 calories: Union[int, float], carbs: Union[int, float]) -> None:
        """ Initialize"""
        self._name = name
        self._weight = weight
        self._calories = calories
        self._carbs = carbs

    @property
    def name(self) -> str:
        """Get the name of this food."""
        return self._name

    @property
    def weight(self) -> Union[int, float]:
        """Get the weight (in grams) of this food."""
        return self._weight

    @property
    def calories(self) -> Union[int, float]:
        """Get the caloric value (calories) of this food."""
        return self._calories

    @property
    def carbs(self) -> Union[int, float]:
        """Get the grams of carbohydrates in this food."""
        return self._carbs

    def percent_carbs(self) -> float:
        """Return the fraction of calories that are carbohydrates.
        1 gram of carbohydrate contains 4 calories.

        :return: fraction of the total calories that are from carbohydrate
        """
        if self.calories == 0 or self.carbs == 0:
            return 0
        return self.carbs * 4 / self.calories

    def __str__(self) -> str:
        return f'{self.name} ({self.weight}g)'

    def __eq__(self, other: object) -> bool:
        """ check that food have the same name and same weight."""
        if not isinstance(other, Food):
            return False
        return self.name == other.name and self.weight == other.weight

    def __add__(self, other: object) -> object:
        """add all thing with same food name"""

        # check that other is food object
        if not isinstance(other, Food):
            raise TypeError("Can only add Food to Food")
        # check that name is equal
        if self.name != other.name:
            raise ValueError("Foods must have the same name")

        return Food(self.name, self.weight + other.weight,
                    self.calories + other.calories, self.carbs + other.carbs)

    def __mul__(self, num: Union[int, float]) -> object:
        # check that num is int or float
        if not isinstance(num, (int, float)):
            raise TypeError("Can only multiply Food by number")
        return Food(self.name, self.weight * num,
                    self.calories * num, self.carbs * num)
    __rmul__ = __mul__  # make a reverse multipy is same result of multiply


# Problem2
class FoodDiary:
    """ A record of foods we consume"""

    def __init__(self) -> None:
        """Initialize of food diary"""
        self.record: List[Food] = []

    def add_food(self, food: Food) -> None:
        """Add a food to the diary.
        If the name of the food matches a food that is already in the diary,
        then add to the quantity of the existing food object
        """
        for each_food in self.record:
            if each_food.name == food.name:
                each_food += food
                return
        self.record.append(food)

    @property
    def calories(self) -> Union[int, float]:
        """ total calories in diary"""
        return sum(food.calories for food in self.record)

    @property
    def carbs(self) -> Union[int, float]:
        """ total grams of carbohydrates in diary"""
        return sum(food.carbs for food in self.record)

    def __str__(self) -> str:
        return f'{len(self.record)} foods with {self.calories:,} calories'

    def percent_carbs(self) -> Union[int, float]:
        """ give the fraction of the total calories from carbohydrates.
        1 gram of carbohydrate provides 4 calories.
        """
        return self.carbs * 4 / self.calories

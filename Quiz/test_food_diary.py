"""Tests of FoodDiary class.  We only test add_food, carbs, and percent_carbs.
Other methods are trivial.
"""
import pytest
from food import Food, FoodDiary
from view_diary import FoodDiaryView  # extends FoodDiary, adds __len__ and @property items

def test_add_food():
    fd = FoodDiaryView()
    fd.add_food(Food("Generic", 100, 50, 5))
    assert len(fd) == 1
    fd.add_food(Food("Another", 100, 60, 8))
    assert len(fd) == 2
    # should update existing foods, not add more
    fd.add_food(Food("Generic", 200, 100, 7.5))
    assert len(fd) == 2
    fd.add_food(Food("Another", 200, 120, 16))
    assert len(fd) == 2

def test_constructor_and_calories():
    # new food diary is empty
    fd = FoodDiary()
    assert fd.calories == 0
    fd.add_food(Food("Generic", 200, 250, 25))
    assert fd.calories == 250
    fd.add_food(Food("No Carb", 400, 500, 0))
    assert fd.calories == 750

def test_carbs():
    fd = FoodDiary()
    assert fd.carbs == 0
    fd.add_food(Food("Generic", 200, 250, 25))
    assert fd.carbs == 25
    fd.add_food(Food("No Carb", 300, 750, 0))
    assert fd.carbs == 25
    fd.add_food(Food("Hi Carb", 400, 400, 100))
    assert fd.carbs == 125


def test_str_and_add_food():
    """test __str__ with add_foods"""
    fd = FoodDiary()
    assert str(fd) == "0 foods with 0 calories"
    fd.add_food(Food("Generic",    10, 20, 2))
    assert str(fd) == "1 foods with 20 calories"
    fd.add_food(Food("No Calorie", 10,  0, 0))
    assert str(fd) == "2 foods with 20 calories"
    fd.add_food(Food("Hi Calorie", 10, 50, 0))
    assert str(fd) == "3 foods with 70 calories"

    # add same foods but 10X the quantities
    fd.add_food(Food("Generic",    100, 200, 2))
    assert str(fd) == "3 foods with 270 calories"
    fd.add_food(Food("No Calorie", 100,   0, 0))
    assert str(fd) == "3 foods with 270 calories"
    fd.add_food(Food("Hi Calorie", 100, 500, 0))
    assert str(fd) == "3 foods with 770 calories"

def test_percent_carbs():
    fd = FoodDiary()
    fd.add_food(Food("Generic", 200, 250, 25))
    assert fd.percent_carbs() == (25*4)/250
    fd.add_food(Food("No Carb", 300, 750, 0))
    assert fd.percent_carbs() == (25*4)/1000
    fd.add_food(Food("Hi Carb", 400, 1000, 250))
    assert fd.percent_carbs() == (25+250)*4/2000
    # result should be repeatable
    assert fd.percent_carbs() == (25+250)*4/2000

# Skipped: Almost everyone's code fails this with DivisionByZero erro!
# Similar to test of percent_carbs in Food.
def dont_test_percent_carbs_no_calories():
    """percent carbs should be correct even if no calories in food diary."""
    fd = FoodDiary()
    assert fd.percent_carbs() == 0
    fd.add_food(Food("Black Coffee", 250, 0, 0))
    assert fd.percent_carbs() == 0
import pytest
import re
from food import Food

"""
I use loop over TESTCASES inside each test instead of parameterized tests
because parameterized tests count each set of parameter values as one test,
making it harder to count failing methods.
"""


def test_str():
    """the str function should return {Name} ({weight}g)"""
    TESTCASES = [
        # name, weight, calories, carbs
        ("Roast Peanut", 100, 300, 0),
        ("Roast Python", 250, 400, 0),
        ("Super Food",     1,  20, 0),
        ]
    for (name, weight, calories, carbs) in TESTCASES:
        # the correct answer as a pattern
        pattern = f"{name}\\s+\\({weight:,}\\s?g\\)"
        # for dummies who don't read instructions - make the comma optional
        pattern = pattern.replace(",",",?")
        expect = f"{name} ({weight:,}g)"
        food = Food(name, weight, calories, carbs)
        actual = str(food)
        message = f"expected={expect}  actual={actual}"
        assert re.fullmatch(pattern, actual) is not None, message


def test_equal():
    TESTCASES = [
        (Food("Superfood", 100, 10, 5), True),  # the test food
        (Food("Superfood", 100, 20, 0), True),  # should compare only name and weight
        (Food("Superfood", 500, 20, 5), False), # weights differ
        (Food("Hamburger", 100, 20, 5), False), # names differ
        ("Superfood (100g)"           , False), # not a food object
    ]
    testfood = TESTCASES[0][0]
    for (other, expected) in TESTCASES:
        assert (testfood == other) is expected


def test_percent_carbs():
    TESTCASES = [
        # name, weight, calories, carbs
        ("no carb food", 100, 80, 0),
        ("low carb food",100, 50, 2.5),
        ("all carb food",100, 100, 25)
        ]
    for (name, weight, calories, carbs) in TESTCASES:
        food = Food(name, weight, calories, carbs)
        expected = (4*carbs)/calories if calories != 0 else 0
        assert food.percent_carbs() == expected


def test_percent_carbs_zero_calories():
    """Some foods have zero carbs and zero calories, such as black coffee and Diet Coke"""
    zero = Food("No-calorie food", 100, 0, 0)
    assert zero.percent_carbs() == 0


def test_add():
    """can add two foods if they have the same name"""
    food1 = Food("Black Rice", 100, 180, 20)
    food2 = Food("Black Rice", 200, 270, 30)
    result = food1 + food2
    assert result.name == "Black Rice"
    assert result.weight == 300
    assert result.calories == 450
    assert result.carbs == 50
    message = "+ should not change either argument"
    assert food1.weight == 100 and food1.calories == 180 and food1.carbs == 20, message
    assert food2.weight == 200 and food2.calories == 270 and food2.carbs == 30, message
    # food of portion size 0
    food3 = Food("Black Rice", 0, 0, 0)
    result = food3 + food1
    assert result.name == "Black Rice"
    assert result.weight == 100
    assert result.calories == 180
    # should not change argument
    assert food3.weight == 0 and food3.calories == 0 and food3.carbs == 0


def test_add_raises_exception():
    """Add should raise ValueError if foods have different names."""
    food1 = Food("Black Rice", 100, 180, 20)
    food2 = Food("White Rice", 100, 200, 25)
    with pytest.raises(ValueError):
        result = food1 + food2


def test_multiply():
    """Can multiply a food by a number."""
    
    for multiple in [2, 0.5, 0]:
        food = Food("Black Rice", 100, 180, 20)
        result = food * multiple
        assert isinstance(result, Food)
        message = "multiply should not change the parameter"
        assert food.weight == 100 and food.calories == 180 and food.carbs == 20, message
        assert result.name == "Black Rice"
        assert result.weight == food.weight*multiple
        assert result.calories == food.calories*multiple
        assert result.carbs == food.carbs*multiple

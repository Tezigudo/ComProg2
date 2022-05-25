from food import Food, FoodDiary

if __name__ == '__main__':
    banana = Food("Banana", 100, 89, 20.2)
    brownrice = Food("Brown rice", 200, 246, 48)
    tofu = Food("Tofu", 100, 104, 2.4)

    for food in [banana, brownrice, tofu]:
        print(f"{food.weight:.0f}g of {food.name} has {food.calories:.0f} calories",
              f"and {food.carbs}g of carbohydrate")

        percent = 100*food.percent_carbs()
        print(f"Carbs are {percent}% of total calories")

    # Test your equal method using different foods and weights
    food1 = Food("Banana", 100, 89, 20.2)
    food2 = Food("Banana", 150, 134, 30.3)

    if food1 == food2:
        print(str(food1), "equals", str(food2))
    else:
        print(str(food1), "not equal", str(food2))

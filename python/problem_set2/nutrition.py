def main():
    # Dictionary of fruits and their calories
    fruits = {
        "apple": 95,
        "avocado": 240,
        "banana": 105,
        "cantaloupe": 60,
        "cherries": 100,
        "grapefruit": 52,
        "grapes": 62,
        "honeydew melon": 64,
        "kiwifruit": 42,
        "lemon": 17,
        "lime": 20,
        "mango": 202,
        "orange": 62,
        "peach": 58,
        "pear": 100,
        "pineapple": 50,
        "plums": 30,
        "strawberries": 4,
        "watermelon": 86
    }

    fruit = input("Fruit: ").strip().lower()

    if fruit in fruits:
        print(f"Calories: {fruits[fruit]}")
    else:
        print() 



main()

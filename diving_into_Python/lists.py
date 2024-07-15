# Lists - this is a collection of multiple items in a single variable
fav_foods = ["pizza", "hotdog", "cake"]
for fav_food in fav_foods:
    print(fav_food, end=" ")

foods = {"drinks": ["soda", "Coffee", "Tea"],
         "dinner": ["Pizza", "Hamburger", "Hotdog"],
         "desert": ["Cake", "ice crem"]
         }
drinks = foods["dinner"][1]
print(drinks)
for drinks in foods["drinks"]:
    print(drinks, end=" ")
print()
for key, values in foods.items():
    for value in values:
        print(value, end=" ")
    print()
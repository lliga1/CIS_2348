# Marianel Liga
# PSID 1394330
# Homework 10.11


class FoodItem:


# TODO: Define constructor with parameters to initialize instance
# attributes (name, fat, carbs, protein)

# implement parameterised constructor
# with attributes name,fat,carbs,protein
    def __init__(self, name, fat, carbs, protein):
        self.name = name
        self.fat = fat
        self.carbs = carbs
        self.protein = protein


# implement default argument constructor
    def __init__(self, name=None, fat=0.0, carbs=0.0, protein=0.0):
        self.name = name
        self.fat = fat
        self.carbs = carbs
        self.protein = protein


# implement get_calories() method with single parameter
    def get_calories(self, num_servings):
# Calorie formula
        calories = ((self.fat * 9) + (self.carbs * 4) + (self.protein * 4)) * num_servings;
        return calories  # return calories value


# implement print_info()
    def print_info(self):
        print('Nutritional information per serving of {}:'.format(self.name))
        print(' Fat: {:.2f} g'.format(self.fat))
        print(' Carbohydrates: {:.2f} g'.format(self.carbs))
        print(' Protein: {:.2f} g'.format(self.protein))

if __name__ == "__main__":
    food_item1 = FoodItem()  # create instance 'food_item1' of FoodItem class
# read input values
    item_name = input()
    amount_fat = float(input())
    amount_carbs = float(input())
    amount_protein = float(input())
# create another instance 'food_item2' of FoodItem class
    food_item2 = FoodItem(item_name, amount_fat, amount_carbs, amount_protein)

    num_servings = float(input())  # read num of servings

    food_item1.print_info()  # calling print_info() method
    print('Number of calories for {:.2f} serving(s): {:.2f}'.format(num_servings, food_item1.get_calories(num_servings)))

    print()

    food_item2.print_info()  # calling print_info() method
    print('Number of calories for {:.2f} serving(s): {:.2f}'.format(num_servings,food_item2.get_calories(num_servings)))
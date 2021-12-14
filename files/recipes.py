from functools import reduce


class Ingredient:

    def __init__(self, name, quantity, measure):
        self.__name = name
        self.__quantity = int(quantity)
        self.__measure = measure

    def get_dict(self, persons=1):
        return {"ingredient_name": self.__name, "quantity": self.__quantity * persons, "measure": self.__measure}

    def get_name(self):
        return self.__name

    def __add__(self, other):
        return Ingredient(self.__name, self.__quantity + other.__quantity, self.__measure)

    def get_quantum(self, persons=1):
        return {"measure": self.__measure, "quantity": self.__quantity * persons}


class Recipe:

    def __init__(self, name):
        self.__name = name
        self.__ingredients = {}

    def read_from_file(self, file):
        i = int(file.readline())
        while 0 < i:
            ingredient = Ingredient(*file.readline().strip().split(" | "))
            self.__ingredients[ingredient.get_name()] = ingredient
            i -= 1
        file.readline()  # read '\n'
        return self

    def get_ingredients_dict(self, persons=1):
        return [i.get_dict(persons) for i in self.__ingredients.values()]

    def get_name(self):
        return self.__name

    def get_ingredients(self):
        return self.__ingredients


class CookBook:

    def __init__(self):
        self.__recipes = {}

    def read_from_file(self, file_name):
        with open(file_name, "r", encoding="UTF-8") as file:
            while True:
                recipe_name = file.readline().strip()
                if '' == recipe_name:
                    return
                self.__recipes[recipe_name] = Recipe(recipe_name.strip()).read_from_file(file)
        return self

    def get_dict(self):
        return {recipe.get_name(): recipe.get_ingredients_dict() for recipe in self.__recipes.values()}

    def print(self):
        print(self.get_dict())

    def get_shop_list(self, dishes, persons):
        ingredients = (r.get_ingredients() for r in
                       map(lambda key: self.__recipes[key], self.__recipes.keys() & set(dishes)))
        shop_list = reduce(
            lambda s, r: dict(list(s.items()) + list(r.items()) + [(k, s[k] + r[k]) for k in set(s) & set(r)]),
            ingredients, {})
        return {i.get_name(): i.get_quantum(persons) for i in shop_list.values()}


cook_book = CookBook()
cook_book.read_from_file("recipes.txt")


def get_shop_list_by_dishes(dishes, person_count):
    return cook_book.get_shop_list(dishes, person_count)


def task1():
    cook_book.print()


def task2():
    print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))


task1()
task2()

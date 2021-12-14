class Pet:

    def __init__(self, type_name, name, weight):
        self._type_name = type_name
        self.__name = name
        self._weight = weight

    def get_name(self):
        return self.__name

    def get_type(self):
        return self._type_name

    def get_weight(self):
        return self._weight

    def say_hello(self):
        """Say hello abstract method"""

    def care(self):
        """Care abstract method"""

    def feed(self):
        self._weight += 1

    def print_info(self):
        print(f"{self._type_name} {self.__name}: {self._weight} кг")


class Bird(Pet):

    def collect_eggs(self):
        self._weight -= 1
        return "Яйцо"

    def care(self):
        return self.collect_eggs()


class Mammal(Pet):

    def milk(self):
        self._weight -= 1
        return "Молоко"

    def care(self):
        return self.milk()


class Goose(Bird):

    def __init__(self, name, weight):
        super().__init__("Гусь", name, weight)

    def say_hello(self):
        return "Га-га-га"


class Cow(Mammal):

    def __init__(self, name, weight):
        super().__init__("Корова", name, weight)

    def say_hello(self):
        return "Муууу"


class Sheep(Pet):

    def __init__(self, name, weight):
        super().__init__("Овца", name, weight)

    def say_hello(self):
        return "Беее"

    def shave(self):
        self._weight -= 1
        return "Шерсть"

    def care(self):
        return self.shave()


class Chicken(Bird):

    def __init__(self, name, weight):
        super().__init__("Курица", name, weight)

    def say_hello(self):
        return "Ко-ко-ко"


class Goat(Mammal):

    def __init__(self, name, weight):
        super().__init__("Коза", name, weight)

    def say_hello(self):
        return "Меее"


class Duck(Bird):

    def __init__(self, name, weight):
        super().__init__("Утка", name, weight)

    def say_hello(self):
        return "Кря-кря"


class Farm:

    def __init__(self, pets):
        self.__pets = pets

    def get_pets(self):
        return self.__pets

    def care_all_pets(self):
        result = []
        for pet in self.__pets:
            result.append(pet.care())
        return result

    def feed_all_pets(self):
        for pet in self.__pets:
            pet.feed()

    def find_pet(self, name):
        for pet in self.__pets:
            if name == pet.get_name():
                return pet

    def stroke(self, pet_name):
        pet = self.find_pet(pet_name)
        if pet is not None:
            print(pet.say_hello())

    def who_is(self, name):
        pet = self.find_pet(name)
        if pet is not None:
            print(pet.get_type())
        else:
            print("Неизвестно")

    def sum_weight(self):
        sum = 0
        for pet in self.__pets:
            sum += pet.get_weight()
        return sum

    def find_pet_max_weight(self):
        mx = 0
        result = None
        for pet in self.__pets:
            if mx < pet.get_weight():
                mx = pet.get_weight()
                result = pet
        return result

    def print_info(self):
        print("Ферма Дядющки Джо:\n-------")
        for pet in self.__pets:
            pet.print_info()


joe_farm = Farm([Goose("Серый", 5), Goose("Белый", 6), Cow("Манька", 200), Sheep("Барашек", 40), Sheep("Кудрявый", 50),
                 Chicken("Ко-ко", 3), Chicken("Кукареку", 4), Goat("Рога", 30), Goat("Копыто", 35), Duck("Кряква", 7)])

joe_farm.print_info()

# Кормим
print("\nКормим..\nКормим..\n")
joe_farm.feed_all_pets()
joe_farm.feed_all_pets()

joe_farm.print_info()

# Ухаживаем
print("Ухаживаем:")
print(joe_farm.care_all_pets())

joe_farm.print_info()

print(f"\nОбщий вес животных: {joe_farm.sum_weight()}")

pet = joe_farm.find_pet_max_weight()
print(f"Самое тяжелое животное:")
pet.print_info()

print("---------")
joe_farm.stroke("Манька")
joe_farm.stroke("Кудрявый")

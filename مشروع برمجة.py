from abc import ABCMeta,abstractmethod
class Zoo:
    animal_count = 0

    def __init__(self, name):
        self.name = name
        self.animals = []


    def add_animal(self, animal):
        self.animals.append(animal)
        Zoo.animal_count += 1
        print(f"Animal '{animal.name}' has been added to the zoo.")

    def show_animals(self):
        if not self.animals:
            print("No animals in the zoo.")
        else:
            for animal in self.animals:
                print(animal.info())

    def feed_all(self):
        for animal in self.animals:
            print(animal.feed())

    def remove_animal(self, name):
        for animal in self.animals:
            if animal.name.lower() == name.lower():
                self.animals.remove(animal)
                Zoo.animal_count -= 1
                print(f"Animal '{name}' has been removed from the zoo.")
                break
        else:
            print(f"No animal named '{name}' found in the zoo.")

    @classmethod
    def total_animals(cls):
        return f"Total animals in the zoo: {cls.animal_count}"

    def __str__(self):
        return f"{self.name} Zoo"


class Entity(metaclass=ABCMeta):
    def __init__(self, name):
        self.name = name
    @abstractmethod
    def describe(self):
        pass


class Animal(Entity):
    def __init__(self, name, age, health_status):
        super().__init__(name)
        self.age = age
        self.is_fed = False
        self.__health_status = health_status

    @property
    def health_status(self):
        return self.__health_status

    @health_status.setter
    def health_status(self, health_condition):
        self.__health_status = health_condition

    def treat(self):
        self.health_status = "Healthy"
        return f"{self.name} has been treated and is now healthy."

    def feed(self):
        self.is_fed = True
        return f"{self.name} has been fed."

    def info(self):
        return f"{self.name} (Age: {self.age}, Health Status: {self.__health_status}, Feeding Status: {self.is_fed})"

    @staticmethod
    def is_young(age):
        return age < 3


    def describe(self):
        return f"This is an entity named {self.name}."

    def __str__(self):
        return f"{self.name} (Age: {self.age})"


zoo = Zoo("Al Zawraa")
cat = Animal("Cat", 5, "Sick")
dog = Animal("Dog", 4, "Healthy")
parrot = Animal("Parrot", 2, "Healthy")

zoo.add_animal(cat)
zoo.add_animal(dog)
zoo.add_animal(parrot)
print()
print(cat.describe())
print(dog.describe())
print(parrot.describe())
print(isinstance(cat,Animal))

while True:
    print("\n--- Zoo Management Menu ---")
    print("1. Feed all animals")
    print("2. Show all animals")
    print("3. Show total number of animals")
    print("4. Treat an animal")
    print("5. Remove an animal")
    print("0. Exit")
    choice = input("Enter a number to perform an action: ")

    if choice == "1":
        zoo.feed_all()
    elif choice == "2":
        zoo.show_animals()
    elif choice == "3":
        print(Zoo.total_animals())
    elif choice == "4":
        animal_name = input("Enter the name of the animal to treat: ")
        for animal in zoo.animals:
            if animal.name.lower() == animal_name.lower():
                print(animal.treat())
                break
        else:
            print(f"No animal named '{animal_name}' found in the zoo.")
    elif choice == "5":
        animal_name = input("Enter the name of the animal to remove: ")
        zoo.remove_animal(animal_name)
    elif choice == "0":
        print("Exiting...")
        break
    else:
        print("Invalid choice, please try again.")





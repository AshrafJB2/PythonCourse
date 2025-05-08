animals_dict = {}


class Zoo:
    def __init__(self, zoo_name):
        self.name = zoo_name
        self.animals = []
    def add_animal(self,new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)
        else:
            print(f"{new_animal} is already in the zoo")
    def get_animals(self):
        print(self.animals)
    def sell_animal(self,animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)
        else:
            print(f"{animal_sold} is not in the zoo")
    def sort_animals(self):
        self.animals.sort()
        for animal in self.animals:
            if animal[0].upper() not in animals_dict:
                animals_dict[animal[0].upper()] = []
            animals_dict[animal[0].upper()].append(animal)

    def get_groups(self):
        for key, value in animals_dict.items():
            print(f"{key}: {value}")


new_york_zoo = Zoo("new_york_zoo")

new_york_zoo.add_animal("cat")
new_york_zoo.add_animal("dog")
new_york_zoo.add_animal("elephant")
new_york_zoo.add_animal("tiger")
new_york_zoo.add_animal("lion")
new_york_zoo.add_animal("bear")
new_york_zoo.add_animal("monkey")
new_york_zoo.add_animal("giraffe")
new_york_zoo.add_animal("zebra")
new_york_zoo.add_animal("horse")
new_york_zoo.add_animal("cow")
new_york_zoo.add_animal("chicken")
new_york_zoo.add_animal("duck")
new_york_zoo.add_animal("goat")
new_york_zoo.add_animal("sheep")
new_york_zoo.add_animal("pig")
new_york_zoo.add_animal("rabbit")
new_york_zoo.add_animal("fish")
new_york_zoo.add_animal("snake")
new_york_zoo.add_animal("crocodile")
new_york_zoo.add_animal("turtle")
new_york_zoo.add_animal("frog")
new_york_zoo.add_animal("hamster")
new_york_zoo.add_animal("mouse")
new_york_zoo.add_animal("rat")
new_york_zoo.add_animal("guinea pig")
new_york_zoo.add_animal("parrot")
new_york_zoo.add_animal("canary")
new_york_zoo.add_animal("cockatiel")

new_york_zoo.get_animals()

new_york_zoo.sell_animal("cat")
new_york_zoo.sell_animal("dog")

new_york_zoo.get_animals()



new_york_zoo.sort_animals()
new_york_zoo.get_groups()

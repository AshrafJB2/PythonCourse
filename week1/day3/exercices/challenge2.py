class Dog:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def bark(self):
        print(f"{self.name} goes woof!")

    def jump(self):
        print(f"{self.name} jumps {self.height * 2} cm high!")


dog1 = Dog("Davids", 80)
dog2 = Dog("Charls", 110)

davids_dog = Dog("Rex", 50)

davids_dog.bark()
davids_dog.jump()

sarahs_dog = Dog("Teacup", 20)

sarahs_dog.bark()
sarahs_dog.jump()

if davids_dog.height > sarahs_dog.height:
    print(f"{davids_dog.name} is bigger")
else:
    print(f"{sarahs_dog.name} is bigger")

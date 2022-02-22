# Создать класс Pet в котором будет реализован метод возвращающий имя животного
#
# Создать класс Cat который наследуется от Pet
# 	Добавить функцию которая печатает в консоль “Мяу”
#
# Создать класс Dog который наследуется от Pet
# 	Добавить функцию которая печатает в консоль “Гав”


class Pet:
    def __init__(self,name):
        self.name = name
    def getName(self):
        return self.name


class Cat(Pet):
    def petSay (self):
        print("Мяу")

class Dog(Pet):
    def petDog(self):
        print("Гав")

dog = Dog("Том")
print(dog.name)
dog.petDog()


cat = Cat("Эрик")
print(cat.name)
cat.petSay()

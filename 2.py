#ввести с консоли 10 слов, если в слове больше 4 букв выводить на печать выражение "короткое слово"
#если слово длинее 4 букв выводить на печать выражение "длинное слово"
# a = 10
# for i in range(a):
#     b = input("Введите  слово ")
#     if 4 < len(b):
#         print("Длинное слово")
#     else:
#         print("Короткое слово")

# dalc(a, b):
#     print(a)
#     print(b)
#     return a + bef c

# print ("Helloy World")
#
# lst = list("gorodminsk")
# print(lst)

# a = [1,2,3,4,5,]
# print(a[::-1])
#
# a = [1,2,3,4,5,]
# a.reverse()
# print(a)

# def change(lst):
#     new_start = lst.pop()
#     new_end = lst.pop(0)
#     lst.append(new_end)
#     lst.insert(0, new_start)
#     return lst
#
#
# print(change([1, 2, 3]))
# print(change([1, 2, 3, 4, 5]))
# print(change(['н', 'л', 'о', 'с']))


# def useless (lst):
#     return max(lst)/ len(lst)
# print(useless([1, 2, 6]))
# print(useless([1, 2, -4, 18, 0, 5]))
# print(useless([-33, -0.05, -4.18, 11.2, 13.12, 55, 7.1]))




# #Разобратся чего так срабатывает
# def list_sort(lst):
#     lst.sort(key=lambda x: abs(x), reverse=True)
#     return lst
#
# print(list_sort([1,2,3,4,5,6,7,8,9,10]))
# print(list_sort([-11,1,2,3,4,5,6,55,7,8,9,789,22,10]))


# def to_float(num):
#     if isinstance(num, (int, float)):
#         return float(num)
#     return "Невозможно преобразовать"
#
# # Тесты
# print(to_float(12))
# print(to_float(-1.762))
# print(to_float(True))
# print(to_float('Не число'))
# print(to_float(2))

# Создать класс Pet в котором будет реализован метод возвращающий имя животного
#
# Создать класс Cat который наследуется от Pet
# 	Добавить функцию которая печатает в консоль “Мяу”
#
# Создать класс Dog который наследуется от Pet
# 	Добавить функцию которая печатает в консоль “Гав”


class Pet:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def getName(self):
        return self.name
    def getAge(self):
        return self.age

class Cat(Pet):
    def petSay (self):
        print("Мяу")

class Dog(Pet):
    def petDog(self):
        print("Гав")

dog = Dog("Том",12)
print(dog.name)
print(dog.age)
dog.petDog()


cat = Cat("Эрик",15)
print(cat.name)
print(cat.age)
cat.petSay()

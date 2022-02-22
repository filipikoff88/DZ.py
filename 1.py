# Нужно сравнить на if
# ввести 10 чисел, если число меньше 5 то их складывать в значение a, если больше пяти то в значени b
# после сложения сравнить числа, если число а будет больше b вывести надписть "А больше B" и наоборот
# print("Введите 10 чисел")
# b = 0
# a = 0
# s = 10
# z = 0
# for i in range(s):
#     print("Введите число № " + str(i + 1))
#     z = input()
#     if int(z) < 5:
#         a += int(z)
#     else:
#         b += int(z)
#
# if a > b:
#     print(" А больше Б")
# else:
#     print("Б больше А ")
#
# print(a)
# print(b)


#Переопределение метода

# z

# Вызов родительского метода

# class A:
#     def do_something(self):
#         print('AA')
# class B(A):
#     def do_something(self):
#      super() .do_something()
#     print('BB')
# obj = B()
# obj.do_something()


#Добовление атрибутов в дочерний класс

# class A:
#     def init__(self, a):
#         self.a = a
# class B(A):
#     def init__(self,a,b):
#         super(). init__(a)
#         self.b = b


#дОБОВЛЕНИЕ атрибутов в дочерний класс

# class A:
#     def __init__(self,a):
#         self.a = a
# class B(A):
#     def __init__(self,a,b):
#         super(). __init__(a)
#         self.b = b

# Задача при инициализации  добовляем 2 элемента
# создать 4 функии которые вводят в консоль результат

# class G:
#     def __init__(self,a,s,f,h):
#         self.a = a
#         self.s = s
#         self.f = f
#         self.h = h

# Функция dir(object)

# class Calc:
#     def sum(self, a, b):
#         print(a+b)
#
# c = Calc()
# #c.sum(1,5)
# print(dir(c))


# class Calc:
#     def sum(self, a, b):
#         print(a+b)
#
#     def minus(self, a,b):
#         print(a-b)


#c = Calc()
#c.sum(1,5)
# print(dir('asdr'))

# Магические методы

# class SomeClass:
#     var = "text"
#
#     def __init__(self, new_var):
#         self.new_var = new_var
#
# a = SomeClass(1)
# b = SomeClass(2)
#
# print(a.new_var, a.var)
#
# print(b.new_var,b.var)


# class SomeClass:
#     var = "your answer:"
#     print(1)
#
#     @classmethod
#     def func(cls,a,b):
#         print(cls.var,a + b)
#
# SomeClass.func(3,7)
# SomeClass.func(6,7)
# SomeClass.func(9,1)

# class SomeClass:
#     var = "your answer:"
#     print(1)
#
#     @classmethod
#     def func(cls,a,b):
#         print(cls.var,a + b)
#
# SomeClass.func(3,7)
# SomeClass.func(6,7)
# SomeClass.func(9,1)

# class Human:
#     def __init__(self, name):
#      self.name = name
#
#     def hello(self):
#         print(F"hello, my name is {self.name}")
#
# a = Human("Pavel")
# a.name = "AE1134"
# a.hello()

class Human:
    def __init__(self, name):
     self.name = name

    def hello(self):
        print(F"hello, my name is {self.name}")

    @classmethod
    def f1(cls):
        print(f" i have{cls.leg_count} legs")

a = Human("Pavel")
a.hello()
Human.f1()
# a.count_leg()
# Human.count_leg()



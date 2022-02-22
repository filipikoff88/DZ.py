# Задание 10.01
# Имеется текстовый файл. Напечатать:
# a) его первую строку;
# b) его пятую строку;
# c) его первые 5 строк;
# d) его строки с s1-й по s2-ю;
# e) весь файл.

# lists = []
# with open('test.txt', 'w') as my_file:
#     my_file.writelines(['строка 1\n', 'строка 2\n', "строка 3\n", "строка 4\n", "строка 5\n", "строка 6\n", "строка 7\n", "строка 8"])

    # for i in range (10):
    #     a = input("введите строки ")
    #     lists.append(a)
    # for list in lists:
    #     my_file.write(list + '/n')

# my_file = open('test.txt')
# while True:
#     line = my_file.readline()
#     if not line:
#         break
#     print(line)
# my_file.close()


my_file = open('test.txt')
my_file2 = open('test2.txt')
itog = 0
scetchik = 0
nomerRaznoiStroki = 0
while True:
    line = my_file.readline()
    line2 = my_file2.readline()

    if line != line2:
        print('Строки в файле разные')
        itog = 1

    scetchik +=1
    if not line:
        break
if itog == 1:
    print("Файлы разные")
else: print("Файлы одинаковые")
my_file.close()
my_file2.close()


# Задание 10.01
# Имеется текстовый файл. Напечатать:
# a) его первую строку;
# b) его пятую строку;
# c) его первые 5 строк;
# d) его строки с s1-й по s2-ю;
# e) весь файл.


with open('test.txt', 'w') as my_file:
    my_file.writelines(['qwerty\n', 'asdf\n', "hhhj\n", "jkjk\n", "hggg\n", "hgtdrd\n", "tyttyty\n", "rrere"])

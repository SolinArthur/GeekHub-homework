#7.Напишите сценарий для объединения всех элементов списка в строку и ее вывода.
# Список должен включать как строки, так и целые числа и должен быть жестко запрограммирован.

spisok = ["gta", 3, 4, 5.15]
viva = " ".join(map(str,spisok))
print(viva)
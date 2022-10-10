# 3.Напишите скрипт, который принимает <number> от пользователя и выводит сумму первых <number>
# положительных целых чисел.

numbers = int(input("Введите число: "))
evrika = 0
for i in range(numbers+1):
    evrika+= i
print(evrika)
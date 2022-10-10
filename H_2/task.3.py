#3.Напишите скрипт, который принимает <number> от пользователя и выводит сумму первых <number>
# положительных целых чисел.

numbers = int(input("Введите число: "))
Evrika = 0
for i in range(numbers+1):
    Evrika = Evrika + i
print(Evrika)
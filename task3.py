# Требуется вывести все целые степени двойки 
# (т.е. числа вида 2**k), не превосходящие числа N.

n = int(input("Введите число: "))
print()
count = 1
while count <= n:
    print(count, end=' ')
    count *= 2
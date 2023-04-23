# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих строках записаны N целых чисел Ai. 
# Последняя строка содержит число X.
# 5
# 1 2 3 4 5
# 6
# -> 5

n = int(input("Введите количество элементов в массиве: "))
num_list = []

for i in range(n):
    num_list.append(int(input("Введите элемент: ")))

print(num_list)
m = int(input("Введите элемент: "))
minDif = abs(m - num_list[0])
neigbor = num_list[0]

for i in range(1, len(num_list)):
    if abs(m - num_list[i]) < minDif:
       minDif =  abs(m - num_list[i]) 
       neigbor = num_list[i]
        

print(neigbor)

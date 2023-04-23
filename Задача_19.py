# Дана последовательность из N целых чисел и число K. 
# Необходимо сдвинуть всю последовательность (сдвиг - циклический) на K элементов вправо, K – положительное число.
# Input: [1, 2, 3, 4, 5] k = 2
# Output: [4, 5, 1, 2, 3]
# Примечание: Пользователь может вводить значения списка или список задан изначально.

# my_list = [1, 2, 3, 4, 5]
# # print(my_list[::]) - срез с шагом 2
# my_list.append(6)
# print(my_list)

# my_list = [1, 2, 3, 4, 5]
# tmp_list = []
# k = 2
# i_tmp = 0

# for i in range(len(my_list)):
#     # if(i > len(my_list)):
#     for i_tmp in range(len(my_list) + k):
#         tmp_list

# Эталонное решение        
# my_list = [1, 2, 3, 4, 5]
# k = 2    
# for i in range(k):
#     my_list.insert(0, my_list.pop())
# print(my_list)

# print(my_list[-k+1:] + my_list[:-k+1])


# Второе решение:
new_list = [1, 2, 3, 4 , 5, 6, 7]
k = int(input("Введите сдвиг: "))
final_list = []

final_list = new_list[-k:] + new_list[:-k]

for i in range(-k, len(new_list) - k):
   final_list.append(new_list[i])

# Способ со срезами:
# my_list = [1, 2, 3, 4, 5]
# k = 6 % len(my_list)

# print(my_list[-k:] + my_list[:-k])

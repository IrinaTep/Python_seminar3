# Напишите программу для печати всех уникальных значений в словаре. 
# Input:  [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII ":" S007 "}] 
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}

# my_dict = {
#     412412: "Стул",
#     645623: "Шкаф",
#     534543: {
#         "Цвет": "Каштан",
#         "Название": "Диван",
#         "Количество": [1, 2, 3]
#     }
# }

# print(my_dict[534543]["Количество"])

# print(412412 in my_dict) - проверка, есть ли такой ключ в my_dict
# print(412412 not in my_dict) - проверка, нет ли такого ключ в my_dict

# # for val in my_dict.keys():
# # for key in my_dict:
# #     print(key)
# Три основных метода:
# Val
# Key
# Item

start_dict = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {" V ": "S009"}, {" VIII ": "S007"}]

result_set = set()

for mini_dict in start_dict:
    result_set = result_set.union(set(mini_dict.values()))

print(result_set)

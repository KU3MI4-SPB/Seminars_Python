# import random

# print(list := [random.randint(0,10) for _ in range(15)])

# new_list = []
# for i in list:
#     if i not in new_list:
#         new_list.append(i)
# print(new_list)


# import random

# print(lst := [random.randint(0,10) for _ in range(5)])

# shift = int(input('Введите сдвиг:'))
# for i in range(len(lst)):
#     print(lst[i % len(lst)] end=' ')


# lst = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII ":" S007 "}]
# val = set()

# for d in lst:
#     for k, v in d.items():
#         val.add(v)

# print(val)

# Дан массив, состоящий из целых чисел. Напишите
# программу, которая подсчитает количество
# элементов массива, больших предыдущего (элемента
# с предыдущим номером)
# Input: [0, -1, 5, 2, 3]
# Output: 2 (-1 < 5, 2 < 3)

array = [0, -1, 5, 2, 3]
count = 0

for i in range(1, len(array)):
    if array[i] > array[i-1]:
        count += 1
        
print(count)

# def find_count(array) -> int:
#     count = 0
#     for i in range(1, len(array)):
#         if array[i] > array[i-1]:
#             count += 1
#     return count

# print(find_count(array))
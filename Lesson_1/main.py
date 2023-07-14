# per_day = 700
# total = 750
# days = total//per_day + (total % per_day != 0)
# print(days)



# room1 = 20
# room2 = 21
# room3 = 22

# total = (room1 + 1)//2 + (room2 + 1)//2 + (room2 + 1)//2
# print(total)



# i = 3
# j = 4

# wagons = 1

# if i == j:
#     print('Без дополнительной информации не определить количество вагонов')
# else:
#     print(f'Количество вагонов: {i + j -1}')



year = int(input("Введите год: "))

if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print("YES")
else:
    print("NO")



from operator import index

my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
index = 0
while index < len(my_list):
    number = my_list[index]
    if number < 0:
        break
    elif number == 0:
        index += 1
        continue
    print(number)
    index += 1
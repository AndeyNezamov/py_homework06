first_number = int(input('Введите превое число: '))
difference = int(input('Введите разность: '))
amount = int(input('Введите колличество: '))
array = []
for i in range(1, amount+1):
    array.append(first_number+(i - 1) * difference)
print(array)
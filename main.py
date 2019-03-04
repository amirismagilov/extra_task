number = int(input('введите число '))
numbers = [number]
i = 1

while number != 0:
    number = int(input('введите число '))
    numbers.append(number)


numbers_sorted = sorted(numbers)
print(numbers)
for number in numbers_sorted[1:]:
    print(i,'.', number)
    i += 1
print('------------')
print('Сумма: ', sum(numbers))å
number = input("Введите число: ")
if number == number[::-1]:
    print("Настоящее")
else:
    print("Кривое")
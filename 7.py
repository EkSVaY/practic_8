s = input("Введите число: ")
while not s.isdigit():
    s = input("Ошибка. Попробуйте ещё раз. Введите число: ")

print(f"Введено целое число: {s}")

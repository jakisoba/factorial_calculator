def factorial(n):
    if n < 0:
        return "Факторіал не визначений для від'ємних чисел"
    elif n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

number = 5
result = factorial(number)
print(f"Факторіал числа {number} дорівнює {result}")

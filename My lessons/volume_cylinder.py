import math


# Объем цилиндра
# PI = math.pi
# # Запрашиваем у пользователя значения радиуса и высоты
# radius = float(input('Введите значение радиуса в см: '))
# height = float(input('Введите значение высоты в см: '))
# # Вычисляем объем цилиндра
# volume = round(PI * radius ** 2 * height, 2)
# print(f'Объем цилиндра равен {volume} куб.см.')


# i = 0
# while i < 6:
#     print('Jimmy five times (' + str(i) + ')')
#     i = i + 1

# def spam (divideBy):
#     try:
#         return 42/divideBy
#     except ZeroDivisionError:
#         print("Error: Invalid argument.")
#
# print(spam(2))
# print(spam(12))
# print(spam(0))
# print(spam(1))
def sum(a, b):
    return a + b


def minus(x, y):
    return x - y


if __name__ == '__main__':
    print(sum(5, 5))
    print(minus(8, 2))

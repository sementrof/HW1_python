a = int(input())
b = int(input())
c = int(input())
# Вычисляем дискриминант
D = b ** 2 - 4 * a * c
# Находим корни уравнения
if D >= 0:
    x1 = (-b + D ** 0.5) / (2 * a)
    x2 = (-b - D ** 0.5) / (2 * a)
    if D == 0:
        print( x1)
    else:
        print( x1,  x2)


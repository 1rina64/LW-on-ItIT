a, b, c = float(input()), float(input()), float(input())
d = b ** 2 - 4 * a * c
print('Ответ:')
if d < 0:
    print('Нет корней')
elif d == 0:
    x = -b / (2 * a)
    print(x)
else:
    x1 = (-b - d ** 0.5) / (2 * a)
    x2 = (-b + d ** 0.5) / (2 * a)
    print(min(x1, x2), max(x1, x2))

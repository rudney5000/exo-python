# 4. Вводятся натуральные M и N.
# Напечатать кубы всех четных чисел из отрезка [M, N].

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    for i in range(a, b - (b % 2) + 1, 2):
        print(i % 2 + i)

# ввод
# 4
# 8

# вход
# 4
# 6
# 8
# 10
# 12
# 14
# 16
# 18
# 20
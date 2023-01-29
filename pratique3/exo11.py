# 11. Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи оно является,
# то есть выведите такое число n, что φn=A.
# Если А не является числом Фибоначчи, выведите число -1.
#
# Входные данные
# Вводится натуральное число.
# Выходные данные
# Выведите ответ на задачу.
# Примеры
# входные данные
# 8
# выходные данные
# 6
# входные данные
# 10
# выходные данные
# -1

def get_fib_ind(n):
    ind = 0
    a, b = 0, 1
    while b <= n:
        ind += 1
        a, b = b, a + b
        if a == n:
            return ind
    return -1


if __name__ == "__main__":
    print(
        get_fib_ind(
            int(input())
        )
    )

# 6. Создать программу, вычисляющую и выводящую на экран сумму цифр натурального числа N.
# N вводится в начале работы программы.

if __name__ == '__main__':
    print(
        sum(
            map(
                int, list(input())
            )
        )
    )
# на ввод: 123456789
# на вход: 45
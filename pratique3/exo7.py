# 7. Начав тренировки, лыжник в первый день пробежал P км.
# Каждый следующий день он увеличивал длину пробега на 10% от пробега предыдущего дня.
# Определить, в какой день он пробежит больше S км.
# P и S вводятся в начале работы программы.
# (Например, для p=10, S=20 должно быть напечатано 2, для p=10, S=200 - 12).

if __name__ == '__main__':
    a = 10
    p = int(input())
    days = 0
    s = 0
    while s < 200:
        a = a + (a * p / 100)
        s += a
        days += 1
    print(days)

# на ввод: 150  // км
# на вход: 3   // количество дня
# 2. Дано целое число, не меньшее 2. Выведите его наименьший натуральный делитель, отличный от 1.
# Входные данные
# Вводится натуральное число.
# Выходные данные
# Выведите ответ на задачу.
# Примеры
# входные данные
# 15
# выходные данные
# 3

def prime_f(n):
    if n % 2 == 0: return 2
    i = 3
    while n % i != 0 and i * i <= n:
        i += 2
    if i * i <= n: return i
    return n


N = int(input())

if __name__ == '__main__':
    print(prime_f(N))

# "C:\Users\Dedy Rudney\exo-dossys\testvenv\Scripts\python.exe" "C:\Users\Dedy Rudney\exo-dossys\pratique3\exo2.py"
# 15
# 3
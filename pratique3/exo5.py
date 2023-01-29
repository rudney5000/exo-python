# 5. Напечатать все трехзначные числа, делящиеся на 3.
# Операцию деления не использовать!


if __name__ == '__main__':
    x = input()
    num = list(map(int, x.split()))
    l = []
    for i in num:
        if i % 3 == 0:
            l.append(i)
    print(*l, sep=" ")

# на ввод 1 2 3 4 5 6 (tu peux ecrire tant de nombre que tu veux mais respect seulement l'espace entre deux nombres)
# на вход 3 6

# if __name__ == '__main__':
    # numbers = input()
    # list = numbers.split()

    # for item in list:
    #     if int(item)%3==0:
    #         list.remove(item)

    # print(' '.join(list))

    # ici il fait sortir tous les nombres qui ne sont pas divisible par 3
    # j'ai ajouté ça parce que le j'ai pas trop compris la question
    # si tu veux le tester il souffit juste de commenter la premiere partie
    # du code et decommente la deuxieme parti du code pour tester
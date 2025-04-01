from random import randint

def roll():
    out=[]
    for i in range(3):
        row = []
        for j in range(3):
            row.append(randint(1, 7))
        out.append(row)
    # for g in out:
        #print("".join(g))
    return out


        


    
def slots(balance, bet):

    if (balance - bet) >= 0:
        out = roll()
        flag = 0
        for i in out:
            if int(i[0]) == int(i[1]) == int(i[2]):
                if int(i[0]) == 7:
                    print("Jeckpot!!!")
                    reward = bet * 10
                    break
                flag = 1
        for g in out:
            print(" ".join(list(map(str, g))))
        if flag == 1:
            reward = bet * 2
            print("Вы выиграли", reward)
        else:
            print("Вы проиграли=(.")
    else:
        print("Ошибка ваш депозит шлишком мал=(")

def defence(a, f, n):
    if f == 1:
        return a
    else:
        return a + n


def black_jack(balance, bet):
    points = 0
    dil_sum = 0
    pl_sum = 0
    dil_sum += randint(1, 11)
    print("Диллер", dil_sum)
    f = 1
    print("Диллер дал вам карты.")
    pl_sum += randint(1, 11)
    print(pl_sum)
    while f > 0:
        if pl_sum == 11:
            defence(pl_sum, f, randint(1, 11))
        else:
            pl_sum += randint(1, 11)
            print(pl_sum)
            otvet = "да"
            while otvet == "да":
                print("Вы хотите взять еще одну карту?")
                otvet = input()
                if otvet == "да":
                    pl_sum += randint(1, 11)
                print(pl_sum)
                if pl_sum > 21:
                    print("Вы проиграли=(")
                    print("Карты диллера:", dil_sum + randint(1, 11))
                    break
        f += 1
        for i in range(2):
            if dil_sum == 11:
                defence(dil_sum, f, randint(1, 11))
                dil_sum += randint(1, 11)
            if dil_sum <= 15:
                if randint(1, 100) >= 25:
                    dil_sum += randint(1, 11)
                    print("Диллер", dil_sum)
            if dil_sum >= 17:
                if randint(1, 100) >= 80:
                    dil_sum += randint(1, 11)
                    print("Диллер", dil_sum)
            if dil_sum <= 14:
                dil_sum += randint(1, 11)
                print("Диллер", dil_sum)
        f = 0
    if dil_sum > pl_sum and dil_sum <= 21:
        print("Вы проиграли=(.")
        print("Итоговые карты диллера: ", dil_sum)
    elif dil_sum == pl_sum:
        print("Нечья")
        print("Диллер", dil_sum)
    else:
        print("Вы выиграли")
        print("Вы",pl_sum)
        

balance = int(input("Введите свой депозит: "))
game = input("Выберите игру: ")
f = int(input("Что бы сделать ставки нажмите 1, для all in нажмите 2.  "))
if f == 1:
    bet = int(input("Введите свою ставку: "))
else:
    bet = balance
while 1 == 1:
    if game == "slots":
        slots(balance, bet)
    else:
        black_jack(balance, bet)
    stop = input("Хотите продолжить? ")
    if stop == "нет":
        break
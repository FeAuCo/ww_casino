import useful


def black_jack(day_balance, bet):
    pl_table = 0
    dil_table = 0
    fair = 0

    fair = useful.fair_checker(fair, day_balance, bet)

    cards = [num for num in range(1, 12) for _ in range(4)]

    for x in range(2):
        if x == 1:
            useful.give_card(1, fair, day_balance, bet, dil_table, cards, pl_table)
        useful.give_card(0, fair, day_balance, bet, dil_table, cards, pl_table)

    answer = input("Вы хотите сделать дабл?\n")
    if answer == "Yes":
        # ПРОВЕРКА БАЛАНСА НА НАЛИЧИЕ ДЕНЕГ ДЛЯ ДАБЛА
        bet *= 2
        useful.give_card(0, fair, day_balance, bet, dil_table, cards, pl_table)
        answer = None
        if pl_table > 21:
            print("У вас перебор")
            day_balance += bet
            return
    else:
        answer = input("Вы хотите взять еще 1 карту?\n")

    while answer == "Yes":
        useful.give_card(0, fair, day_balance, bet, dil_table, cards, pl_table)
        if pl_table > 21:
            print("У вас перебор")
            day_balance += bet
            return
        answer = input("Вы хотите взять еще 1 карту?\n")

    while dil_table < pl_table and (pl_table != dil_table and useful.checker(cards, dil_table) < 0.5):
        useful.give_card(1, fair, day_balance, bet, dil_table, cards, pl_table)
        if dil_table > 21:
            print("У диллера перебор, вы выиграли ", bet * 2)
            day_balance -= bet
            return

    if pl_table == dil_table:
        print("Ничья вы вернули ставку")
        # НАДО В БД ВЕРНУТЬ СТАВКУ!!!!

    elif dil_table > pl_table:
        print("Вы проиграли ", bet)

    else:
        print("Вы выиграли ", bet * 2)

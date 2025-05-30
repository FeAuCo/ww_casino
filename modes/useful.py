import random


def fair_checker(fair, day_balance, bet):
    if day_balance * 0.3 > bet:
        fair = 1

    return fair


def give_card(entity, fair, day_balance, bet, dil_table, cards, pl_table):
    fair_checker(fair, day_balance, bet)

    if entity == 1:
        dil_card = random.choice(cards)
        while dil_table + dil_card > 21:
            if fair == 1:
                break
            dil_card = random.choice(cards)
        cards.remove(dil_card)
        if dil_card == 11 and dil_table + 11 > 21:
            dil_table += 1
        else:
            dil_table += dil_card

        print("Диллеру выдана карта ", dil_card, " общая сумма ", dil_table)
    else:
        pl_card = random.choice(cards)
        while pl_table + pl_card == 21:
            if fair == 1:
                break
            pl_card = random.choice(cards)
        cards.remove(pl_card)
        if pl_card == 11 and pl_table + 11 > 21:
            pl_table += 1
        else:
            pl_table += pl_card
        print("Игроку выдана карта ", pl_card, " общая сумма ", pl_table)

    return pl_table, dil_table


def checker(current_list, sum_cards):
    good = 0
    for i in current_list:
        if i + sum_cards < 21:
            good += 1
    return good / len(current_list)

import random


def drawCard():
    """
    Returns an element from the cards Array.
    :return: The number referencing a card.
    """
    return cards[random.randint(0, len(cards) - 1)]


def countHand(array):
    """
    Sum cards in player's hand and returns it.
    :param array: All the cards that a player have.
    :return: Sum of all cards in player's hand.
    """
    handSum = 0
    for card in array:
        handSum += card
    if handSum > 21 & 11 in array:
        handSum -= 10
    return handSum


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
pcCards = [drawCard(), drawCard()]
userCards = [drawCard(), drawCard()]

isOver = False
while not isOver:
    output = [pcCards[0]] + ['hidden'] * (len(pcCards) - 1)
    print(f"The Computer's hand is: {output}")
    print(f"Your hand is: {userCards}")
    choice = input("Would you like to draw a card? Type 'y' for yes, or 'n' for no: ")
    if choice.strip().lower() == 'y':
        userCards.append(drawCard())
        if countHand(userCards) > 21:
            isOver = True
            print(f"Your hand is now {userCards}. It is over 21. You lost.")
    else:
        isOver = True
        pcCount = countHand(pcCards)
        userCount = countHand(userCards)
        if pcCount < 17:
            pcCards.append(drawCard())
            print(f"The computer hand was less than 17. Drawing another card...")
        if userCount == pcCount:
            print(f"The pc hand was {pcCards}. Your hand was {userCards}. Draw!")
        elif userCount > pcCount:
            print(f"The pc hand was {pcCards}. Your hand was {userCards}. You Won!")
        elif userCount < pcCount:
            print(f"The pc hand was {pcCards}. Your hand was {userCards}. You Lost!")
        else:
            print('IDK')

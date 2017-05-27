#coding: utf-8

# 2. Реализовать класс(ы) для работы с карточной колодой, который предоставляет методы:
# - инициализация заданным числом карт (36 или 52)
# - получение карты (карта должна пропадать из колоды после того, как была получена)
# - сравнение двух карт (при это учесть, что туз > король > дама > валет > числовые карты)
# - получение оставшегося числа карт в колоде
# Не забыть про то, что каждая карта имеет масть.

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    #  в колоде будет 52 карты
    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7',
                  '8', '9', '10', 'Jack', 'Queen', 'King']

    def __str__(self):
        return '%s of %s' % (Card.rank_names[self.rank],
                             Card.suit_names[self.suit])

    def __cmp__(self, other):
        # сравнение мастей
        if self.suit > other.suit: return 1
        if self.suit < other.suit: return -1
        # сравнение рангов
        if self.rank > other.rank: return 1
        if self.rank < other.rank: return -1
        # масть и ранг совпадают
        return 0

class Deck:
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                card = Card(suit, rank)
                self.cards.append(card)

    def delete_card(self):
    # получение карты (удаление из колоды и вывод ее масти и ранга)
        return self.cards.pop()

    def left_card(self):
    # получение числа карт в колоде
        return len(self.cards)

# для проверки
#r1 = Card(1, 11)
#r2 = Card(2, 10)

#r3 = Deck()

#print(r1)
#print(r3.left_card())
#print(r3.delete_card())
#print(r3.left_card())

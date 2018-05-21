import random

class Card(object):
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

# card = Card('Spades', 'Ace')
# print card
# print card.suit
# print card.value

class Deck(object):
    def __init__(self):
        # build the deck of card objects
        self.deck = []
        self.reset()


    def reset(self):
        self.deck = []
        suits =['Clubs', 'Spades', 'Diamonds', 'Hearts']
        for suit in suits: 
            for i in range(2,15): 
                value = i
                if i == 11:
                    value = 'Jack'
                elif i == 12:
                    value = 'Queen'
                elif i == 13:
                    value = 'King'
                elif i == 14:
                    value = 'Ace' 
                self.deck.append(Card(suit, value))

    def display(self):
        for card in self.deck:
            print "{} of {}".format(card.value, card.suit)

    def shuffle(self):
        random.shuffle(self.deck)


deck = Deck() 
deck.shuffle()
deck.display()



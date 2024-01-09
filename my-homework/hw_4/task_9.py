class CardDeck:
    def __init__(self):
        # initialize the suits and ranks for the deck
        self.suits = ['clubs', 'diamonds', 'hearts', 'spades']
        self.ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
        # create a list of all possible cards in the deck
        self.cards = [(suit, rank) for suit in self.suits for rank in self.ranks]
        # initialize the current index for tracking the iteration progress
        self.current_index = 0

    def __iter__(self): # make the object iterable
        return self

    def __next__(self): # iterate over the cards and return the next card as a string
        if self.current_index < len(self.cards):
            card = self.cards[self.current_index]
            self.current_index += 1
            return f"{card[0]} {card[1]}"
        else:
            # raise StopIteration when all cards have been iterated
            raise StopIteration

# create a deck object
deck = CardDeck()

# iterate through the deck and print each card
for card in deck:
    print(card)

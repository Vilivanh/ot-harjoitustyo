from deck import Deck, Hand

class Play:
    def __init__(self):
        self.deck = Deck()
        self.player = Hand()
        self.computer = Hand()
        self.deck.shuffle()

        
    def deal(self,players_number):
        deck = self.deck
        PlayerHand = []
        ComputerHands = []
        for i in range(1,players_number):
            ComputerHands.append([])
        while len(deck.cards) > 0:
            for i in range(players_number):
                if i == 0:
                    PlayerHand.append(self.deck.cards[0])
                    self.deck.cards.pop(0)
                else:
                    if len(deck.cards) > 0:
                        ComputerHands[i-1].append(self.deck.cards[0])
                        self.deck.cards.pop(0)
        return PlayerHand,ComputerHands

        
        

        
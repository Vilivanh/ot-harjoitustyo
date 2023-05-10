from handlers import Handlers

class ComputerChoose:
    """
    Class aims to handle, how computer chooses which card to play
    """
    def __init__(self):
        self.hand = []
        self.tabledeck = []
        
    def emptytable(self, hand):
        """
        chooses which card to play, when table does not have any cards
        aim is to choose the smalles card, assuming that it is heart or spade
        diamonds should be played only when there is nothing else to play
        """
        chosen = None
        for i in range(len(hand)):
            rank = Handlers().rank_integer(hand[i][0])
            suit = hand[i][1]
            if chosen == None:
                chosen = (rank, suit)
            else:
                if chosen[1] == "diamond":
                    if suit == "spade":
                        chosen = (rank, suit)
                    elif suit == "heart":
                        chosen = (rank, suit)
                    elif suit == "club":
                        chosen = (rank, suit)
                    else:
                        chosenrank = Handlers().rank_integer(chosen[0])
                        if int(chosenrank) > int(rank):
                            chosen = (hand[i][0], suit)
                elif chosen[1] == "club":
                    if suit == "spade" or "heart":
                        chosen = (hand[i][0], suit)
                    elif suit == "club":
                        chosenrank = Handlers().rank_integer(chosen[0])
                        if int(chosenrank) > int(rank):
                            chosen = (hand[i][0], suit)            
                elif chosen[1] == "heart":
                    if suit == chosen[1]:
                        chosenrank = Handlers().rank_integer(chosen[0])
                        if int(chosenrank) > int(rank):
                            chosen = (hand[i][0], suit)
                elif chosen[1] == "spade":
                    if suit == chosen[1]:
                        chosenrank = Handlers().rank_integer(chosen[0])
                        if int(chosenrank) > int(rank):
                            chosen = (hand[i][0], suit)                        
        return chosen
    def nonempty(self, tabledeck, hand, players_number):
        """
        chooses which card to play, when table has cards
        if table's top card is spade, heart or club, play higher of these
        if top card is high spade or heart, play small diamond
        """
        top_card = tabledeck[-1]
        toprank = Handlers().rank_integer(top_card[0])
        topsuit = top_card[1]
        chosen = None
        print(hand)
        for i in range(len(hand)):
            givenrank = hand[i][0]
            rank = Handlers().rank_integer(givenrank)
            suit = hand[i][1]
            if chosen == None:
                if suit == topsuit:
                    if int(rank) > int(toprank):
                        rank = Handlers().rank_fixer(str(rank))
                        chosen = (rank, suit)
            else:
                if suit == topsuit:
                    if int(rank) > int(toprank):
                        if chosen[1] == topsuit:
                            chosenrank = Handlers().rank_integer(chosen[0])
                            if int(chosenrank) > int(rank):
                                rank = str(Handlers().rank_fixer(rank))
                                chosen = (rank, suit)
                        elif chosen[1] == "diamond":
                            chosen = (hand[i][0], suit)
                elif topsuit == "spade":
                    if int(toprank) > 11:
                        if chosen == None:
                            if suit == "diamond":
                                if int(rank) < 5:
                                    chosen = (hand[i][0], suit)
                                if len(tabledeck) == players_number - 1:
                                    chosen = (hand[i][0], suit)
                                if len(hand) < 3:
                                    chosen = (hand[i][0], suit)
                elif topsuit == "heart":
                    if int(toprank) > 11:
                        if chosen == None:
                            if suit == "diamond":
                                if int(rank) < 5:
                                    chosen = (hand[i][0], suit)
                                if len(tabledeck) == players_number - 1:
                                    chosen = (hand[i][0], suit)
                                if len(hand) < 3:
                                    chosen = (hand[i][0], suit)
        return chosen
import itertools, random

class Methods:
    def shuffle():
        players = 4
        starter = None
        playerlists = []
        for i in range(players):
            playerlists.append([])
        #0 = club, 1=heart, 2=spade, 3=diamond
        deck = list(itertools.product(range(2,15),['0','1','2','3']))
        random.shuffle(deck)
        while len(deck)>0:
            for i in range(players):
                playerlists[i].append(deck[0])
                deck.pop(0)
        for i in range(players):
            if (2,'0') in playerlists[i]:
                starter = f"pelaaja {i}"
            print(f"pelaaja {i}")
            print(playerlists[i])
            print("\n")
        print(starter)
        return starter, playerlists



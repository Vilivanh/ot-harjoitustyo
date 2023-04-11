import itertools, random

class Methods:
    def shuffling(players_number):
        players = players_number
        starter = None
        player_names = []
        playerlists = []
        for i in range(players):
            playerlists.append([])
        #0 = club, 1=heart, 2=spade, 3=diamond
        r = []
        for i in range(2,11):
            r.append(str(i))
        r.append("jack")
        r.append("queen")
        r.append("king")
        r.append("ace")
        l = ["club","heart","spade","diamond"]
        deck = list(itertools.product(r,l))

        random.shuffle(deck)
        while len(deck)>0:
            for i in range(len(playerlists)):
                playerlists[i].append(deck[0])
                deck.pop(0)
                if len(deck) == 0:
                    
                    for i in range(len(playerlists)):
                        if i == 0:
                            player_names.append("Manual")
                        else:
                            player_names.append(f"computer_player_{i}")    
                        if ('2','club') in playerlists[i]:
                            starter = f"pelaaja {i}"
                        print(f"pelaaja {i}")
                        print(playerlists[i])
                    print(player_names)
                    print("\n")
                    print(starter)
                    return starter, playerlists



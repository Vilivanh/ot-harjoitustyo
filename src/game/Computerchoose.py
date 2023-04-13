class ComputerChoose:
    def emptytable(hand):
        chosen = None
        for i in range(len(hand)):
            rank = hand[i][0]
            if rank == "jack":
                rank = "11"
            elif rank == "queen":
                rank = "12"
            elif rank == "king":
                rank = "13"
            elif rank == "ace":
                rank = "14"
            suit = hand[i][1]
            if chosen == None:
                chosen = (hand[i][0], suit)
            else:
                if chosen[1] == "diamond":
                    if suit == "spade":
                        chosen = (hand[i][0], suit)
                    elif suit == "heart":
                        chosen = (hand[i][0], suit)
                    elif suit == "club":
                        chosen = (hand[i][0], suit)
                    else:
                        chosenrank = chosen[0]
                        if chosenrank == "jack":
                            chosenrank = "11"
                        elif chosenrank == "queen":
                            chosenrank = "12"
                        elif chosenrank == "king":
                            chosenrank = "13"
                        elif chosenrank == "ace":
                            chosenrank = "14"
                        if int(chosenrank) > int(rank):
                            chosen = (hand[i][0], suit)
                elif chosen[1] == "club":
                    if suit == "spade" or "heart":
                        chosen = (hand[i][0], suit)
                    elif suit == "club":
                        chosenrank = chosen[0]
                        if chosenrank == "jack":
                            chosenrank = "11"
                        elif chosenrank == "queen":
                            chosenrank = "12"
                        elif chosenrank == "king":
                            chosenrank = "13"
                        elif chosenrank == "ace":
                            chosenrank = "14"
                        if int(chosenrank) > int(rank):
                            chosen = (hand[i][0], suit)
                        
                elif chosen[1] == "heart":
                    if suit == chosen[1]:
                        chosenrank = chosen[0]
                        if chosenrank == "jack":
                            chosenrank = "11"
                        elif chosenrank == "queen":
                            chosenrank = "12"
                        elif chosenrank == "king":
                            chosenrank = "13"
                        elif chosenrank == "ace":
                            chosenrank = "14"
                        if int(chosenrank) > int(rank):
                            chosen = (hand[i][0], suit)
                elif chosen[1] == "spade":
                    if suit == chosen[1]:
                        chosenrank = chosen[0]
                        if chosenrank == "jack":
                            chosenrank = "11"
                        elif chosenrank == "queen":
                            chosenrank = "12"
                        elif chosenrank == "king":
                            chosenrank = "13"
                        elif chosenrank == "ace":
                            chosenrank = "14"
                        if int(chosenrank) > int(rank):
                            chosen = (hand[i][0], suit)

                        
        return chosen

    def nonempty(self, tabledeck, hand):
        top_card = tabledeck[-1]
        toprank = top_card[0]
        if toprank == "jack":
            toprank = "11"
        if toprank == "queen":
            toprank = "12"
        if toprank == "king":
            toprank = "13"
        if toprank == "ace":
            toprank = "14"
        topsuit = top_card[1]
        chosen = None
        for i in range(len(hand)):
            rank = hand[i][0]
            if rank == "jack":
                rank = "11"
            if rank == "queen":
                rank = "12"
            if rank == "king":
                rank = "13"
            if rank == "ace":
                rank = "14"
            suit = hand[i][1]
            if chosen == None:
                if suit == topsuit:
                    if int(rank) > int(toprank):
                        if rank == "11":
                            rank = "jack"
                        elif rank == "12":
                            rank = "queen"
                        elif rank == "13":
                            rank = "king"
                        elif rank == "14":
                            rank = "ace"
                        chosen = (rank, suit)
            else:
                if suit == topsuit:
                    if int(rank) > int(toprank):
                        if chosen[1] == topsuit:
                            if chosen[0] == "jack":
                                chosenrank = "11"
                            elif chosen[0] == "queen":
                                chosenrank = "12"
                            elif chosen[0] == "king":
                                chosenrank = "13"
                            elif chosen[0] == "ace":
                                chosenrank = "14"
                            else:
                                chosenrank = chosen[0]
                            if int(chosenrank) > int(rank):
                                if rank == "11":
                                    rank = "jack"
                                elif rank == "12":
                                    rank = "queen"
                                elif rank == "13":
                                    rank = "king"
                                elif rank == "14":
                                    rank = "ace"
                                else:
                                    rank = f"{rank}"

                                chosen = (rank, suit)
                        elif chosen[1] == "diamond":
                            chosen = (hand[i][0], suit)
                elif topsuit == "spade":
                    if int(toprank) > 11:
                        if chosen == None:
                            if suit == "diamond":
                                if int(rank) < 5:
                                    chosen = (hand[i][0], suit)
                elif topsuit == "heart":
                    if int(toprank) > 11:
                        if chosen == None:
                            if suit == "diamond":
                                if int(rank) < 5:
                                    chosen = (hand[i][0], suit)
        return chosen
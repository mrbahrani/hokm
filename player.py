class Player:
    def __init__(self, name, iden):
        self.conection = None
        self.session = None
        self.name = name
        self.playerID=iden
        self.game=None
        self.playerCards=[]

    def showCards(self):
        print(self.name," Your Cards :")
        for i in range(len(self.playerCards)):
            print(i, ")", self.playerCards[i])

    def chooseHokm(self):
        self.showCards()
        hokm=input("input H for heart, D for diamond, S for spade, C for club: ")
        return hokm.upper()

    def drop(self,numberofDrops):
        for i in range(numberofDrops):
            self.showCards()
            dropIndex = int(input("which card do you want to drop: "))
            yield self.playerCards.pop(dropIndex)

    def droptemp(self,card1,card2, last = False):
        if not last:
            answer1=input("%s do you want it? y/n" %card1).upper()
            if answer1=="Y":
                self.playerCards.append(card1)
                return card2
            else:
                print("you chose " , card2)
                self.playerCards.append(card2)
                return card1
        else:
            answer1 = input("you have 1)%s and 2)%s which one do you want? 1/2" %(card1,card2))
            if answer1=="1":
                self.playerCards.append(card1)
                return card2
            else:
                self.playerCards.append(card2)
                return card1
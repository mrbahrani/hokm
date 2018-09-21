import game
from random import randint
from player import Player
class Game2(game.Game):
    def __init__(self,iden):
        super(Game2,self).__init__(iden)
        self.numberOfplayers=2
        self.nothakem= Player(0,"patoxi")
    def chooseHakem(self):
        if self.roundNumber==1:
            r = randint(0,1)
            self.hakem =self.playerlist[r]
        else:
            self.hakem=self.winner
        print("GAME = hakem is ", self.hakem.name)

    def initHand(self):
        for player in self.playerlist:
            for i in range(5):
                r = randint(0,len(self.cards))
                player.playerCards.append(self.cards.pop(r))

        self.hokm=self.hakem.chooseHokm()
        self.outOfGameCards += list(self.hakem.drop(3))
        self.outOfGameCards += list(self.notHakem.drop(2))
        print("GAME= hokm is",self.hokm)


    def hand(self):
        self.turn = self.hakem
        for i in range((len(self.cards)//2)-1):
            print("its ",self.turn.name,"turn :")
            r = randint(0,len(self.cards)-1)
            card1=self.cards.pop(r)
            r = randint(0,len(self.cards)-1)
            card2=self.cards.pop(r)
            if self.turn == self.hakem:
                droped = self.hakem.droptemp(card1,card2)
                self.outOfGameCards.append(droped)
                self.turn = self.notHakem
            else:
                droped = self.notHakem.droptemp(card1,card2)
                self.outOfGameCards.append(droped)
                self.turn = self.hakem
        print("its ", self.turn.name, "turn :")
        r = randint(0, len(self.cards) - 1)
        card1 = self.cards.pop(r)
        r = randint(0, len(self.cards) - 1)
        card2 = self.cards.pop(r)
        droped = self.hakem.droptemp(card1, card2,True)
        self.outOfGameCards.append(droped)

    def run(self):
        self.roundNumber+=1
        self.chooseHakem()
        self.notHakem = self.playerlist[(self.playerlist.index(self.hakem) + 1) % 2]
        self.initHand()
        self.hand()
        print(self.cards)
        print(self.outOfGameCards)
        self.hakem.showCards()
        self.notHakem.showCards()


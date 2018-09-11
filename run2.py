from player import Player
from game2 import Game2

p1 = Player("Ali", 1)
p2 = Player("Maahhi", 2)

game = Game2(1)
game.playerlist.append(p1)
game.playerlist.append(p2)
game.run()
from enum import Enum
import numpy as np


class coin(Enum):
    '''outcome of coin flip; heads or tails'''

    HEADS = 0
    TAILS = 1

class Game(object):
    def __init__(self, id):
        self._id = id
        self._flip= 1
        self._total_flip=20
        self._wins=0
        self._number_tails=0
        self._currentSide = coin.HEADS

        self._rnd = np.random
        self._rnd.seed(self._id)

    def next_flip(self):
        if self._currentSide == coin.HEADS:
            if self._rnd.random_sample() < .5:
                self._currentSide = coin.HEADS
                self._number_tails=0
            if self._rnd.random_sample() > .5:
                self._currentSide = coin.TAILS
                self._number_tails = 1

        elif self._currentSide == coin.heads:
            if self._rnd.random_sample() > .4:
                self._currentSide = coin.TAILS
                self._number_tails=1
            if self._rnd.random_sample() < .4:
                if self._number_tails >= 2:
                    self._wins +=1
                    self._currentSide = coin.HEADS
                    self._number_tails =0
        self._flip += 1

    def play(self):
        for i in range(1, self._total_flip +1):
            self._rnd = np.random
            self._rnd.seed (self._id* self._flip)
            self.next_flip()

    def payout(self):
        self.play()
        self._reward = -250 +(100* self._wins)
        return self._reward



class GroupOfGames:
    def __init__(self, id, numPlayers):
        self._list_players = []
        n=1

        while n <= 1000:
            player = Game(id=id * numPlayers + n)
            self._list_players.append(player)
            n+=1
    def Simulation(self):
        GameRewards = []
        for player in self._list_players:
            GameRewards.append(player.payout())
        return sum(GameRewards)/(1000)

trial1=GroupOfGames(id=1, numPlayers =1000)
print (trial1.Simulation())








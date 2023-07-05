from dataclasses import dataclass

actions = {
    'none': 0,
    'rock': 1,
    'paper': 2,
    'scissors': 3,
    'nuclear bomb': 4
}
@dataclass
class PlayerInfo:

    name: str
    current_action: int = 0



class Player:

    def __init__(self, playerinfo):
        self.playerinfo = playerinfo

    def take_move(self):
        print(f'{self.playerinfo.name}')
        move = int(input('[1] rock, [2] paper, [3] scissors'))
        self.playerinfo.current_action = move


def comparison(move1, move2):
    if move1 == 1:
        if move2 == 1:
            result = 'draw'
        elif move2 == 2:
            result = 'loss'
        elif move2 == 3:
            result = 'win'

    if move1 == 2:
        if move2 == 1:
            result = 'win'
        elif move2 == 2:
            result = 'draw'
        elif move2 == 3:
            result = 'loss'

    if move1 == 3:
        if move2 == 1:
            result = 'loss'
        elif move2 == 2:
            result = 'win'
        elif move2 == 3:
            result = 'draw'

    return result

class Game:

    def __init__(self, players):
        self.players = players



    def check_moves(self):
        left = 0
        results = []
        for i, player in enumerate(self.players):

            right = len(self.players) - 1
            while i < right:
                result = [(self.players[i].playerinfo.name, self.players[right].playerinfo.name), comparison(self.players[i].playerinfo.current_action, self.players[right].playerinfo.current_action)]
                results.append(result)
                right -= 1

        print(f'{[result for result in results]}')
        print(len(results))



players = []

no_players = int(input('how many players? '))

for i in range(no_players):
    pinfo = PlayerInfo(input('Enter a name: '))
    curr_player = Player(pinfo)
    players.append(curr_player)

print(players)
print(players[0].playerinfo.current_action)
game = Game(players)
while True:

    for player in players:

        player.take_move()

    game.check_moves()

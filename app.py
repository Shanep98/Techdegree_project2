import constants

import copy

players = copy.deepcopy(constants.PLAYERS)
teams = copy.deepcopy(constants.TEAMS)

print(players)

def set_exp():
    for player in players:
        exp = player["experience"]
        if exp == "YES":
            player["experience"] = True
        else:
            player["experience"] = False


def set_height():
    for player in players:
        player_inches = player["height"].split(" ")
        player_height_num = int(player_inches[0])
        player["height"] = player_height_num


def player_guardians():
    for player in players:
        player["guardians"] = player["guardians"].split(" and ")


set_exp()
set_height()
player_guardians()

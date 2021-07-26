import constants

import copy

import sys



players = copy.deepcopy(constants.PLAYERS)
teams = copy.deepcopy(constants.TEAMS)
Panthers = []
Bandits = []
Warriors = []
p_total_height = 0
b_total_height = 0
w_total_height = 0


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


def balance_teams():
    players_per_team = len(players) / len(teams)
    halfway_point = players_per_team / 2
    #help with setting up evenly dividing players based on experience
    for player in players:
        if player["experience"] == True:
            if len(Panthers) != halfway_point:
                Panthers.append(player)
            elif len(Bandits) != halfway_point:
                Bandits.append(player)
            elif len(Warriors) != halfway_point:
                Warriors.append(player)

    if len(Warriors) == halfway_point:
        for player in players:
            if player["experience"] == False:
                if len(Panthers) != players_per_team:
                    Panthers.append(player)
                elif len(Bandits) != players_per_team:
                    Bandits.append(player)
                elif len(Warriors) != players_per_team:
                    Warriors.append(player)


def average_height():
    p_total_height = 0
    b_total_height = 0
    w_total_height = 0
    for player in Panthers:
        p_total_height += player["height"]
    p_total_height /= len(players)

    for player in Bandits:
        b_total_height += player["height"]
    b_total_height /= len(players)

    for player in Warriors:
        w_total_height += player["height"]
    w_total_height /= len(players)

    return p_total_height
    return b_total_height
    return w_total_height


set_exp()
set_height()
player_guardians()
balance_teams()
average_height()


if __name__ == "__main__":

    print("hello world")
    print("BASKETBALL TEAM STATS TOOL")
    print("----Menu----")
    print("Here are your choices:" '\n' "A) Display Team Stats" '\n' "B) Quit")
    test = input("Enter an option:  ")
    test = test.lower()
    if test == 'b':
        sys.exit("Thank you for using BASKETBALL TEAM STATS TOOL.")

    if test == 'a':
        while True:
            print("The teams that we have available are:" '\n' "A) Panthers" '\n' "B) Bandits" '\n' "C) Warriors")
            test2 = input("Which team would you like to see?  ")
            test2 = test2.lower()
            if test2 == 'a':
                print("Team: Panthers Stats"'\n' "--------------"'\n'"Total players: {}".format(len(Panthers)))
                print("Players on Team: ")
                for player in Panthers:
                    print(player['name'])
                test3 = input("Would you like to view another team?   ")
                if test3 == 'no':
                    sys.exit("Thank you for using BASKETBALL TEAM STATS TOOL.")
                if test3 == 'yes':
                    continue
                else:
                    print("That is unfortunately not a supported option.")
                    test3 = input("Would you like to view another team?   ")
                    continue

            if test2 == 'b':
                print("Team: Bandits Stats"'\n' "--------------"'\n'"Total players: {}".format(len(Bandits)))
                print("Players on Team: ")
                for player in Bandits:
                    print(player['name'])
                test3 = input("Would you like to view another team?   ")
                if test3 == 'no':
                    sys.exit("Thank you for using BASKETBALL TEAM STATS TOOL.")
                if test3 == 'yes':
                    continue
                else:
                    print("That is unfortunately not a supported option.")
                    test3 = input("Would you like to view another team?   ")
                    continue

            if test2 == 'c':
                print("Team: Warriors Stats"'\n' "--------------"'\n'"Total players: {}".format(len(Warriors)))
                print("Players on Team: ")
                for player in Warriors:
                    print(player['name'])
                test3 = input("Would you like to view another team?   ")
                if test3 == 'no':
                    sys.exit("Thank you for using BASKETBALL TEAM STATS TOOL.")
                if test3 == 'yes':
                    continue
                else:
                    print("That is unfortunately not a supported option.")
                    test3 = input("Would you like to view another team?   ")
                    continue

            if test2 != 'a' 'b' 'c':
                print("That is unfortunately not a supported option.")
                continue

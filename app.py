import constants

import copy

import sys


players = copy.deepcopy(constants.PLAYERS)
teams = copy.deepcopy(constants.TEAMS)
Panthers = []
Bandits = []
Warriors = []


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


def average_height(team):
    a_height = 0
    for player in team:
        a_height += player['height']
    a_height /= len(team)
    return a_height


if __name__ == "__main__":


    set_exp()
    set_height()
    player_guardians()
    balance_teams()


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
                count_exp = 0
                count_inexp = 0
                for player in Panthers:
                    if player['experience'] == True:
                        count_exp += 1
                    else:
                        count_inexp += 1
                print('Total experienced: {}'.format(count_exp))
                print('Total inexperienced: {}'.format(count_inexp))
                a_h = average_height(Panthers)
                print('Average height: {}'.format(a_h))
                print("Players on Team: ")
                names_together =  []
                for player in Panthers:
                    names = player['name']
                    names_together.append(str(names))
                print(", ".join(names_together))
                print('Guardians: ')
                guardians_together =  []
                for player in Panthers:
                    names = ', '.join(player['guardians'])
                    guardians_together.append(names)
                print(', '.join(guardians_together))
                print('\n')
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
                count_exp = 0
                count_inexp = 0
                for player in Bandits:
                    if player['experience'] == True:
                        count_exp += 1
                    else:
                        count_inexp += 1
                print('Total experienced: {}'.format(count_exp))
                print('Total inexperienced: {}'.format(count_inexp))
                a_h = average_height(Bandits)
                print('Average height: {}'.format(a_h))
                print("Players on Team: ")
                names_together =  []
                for player in Bandits:
                    names = player['name']
                    names_together.append(str(names))
                print("  " ", ".join(names_together))
                print('Guardians: ')
                names_together =  []
                for player in Bandits:
                    names = player['name']
                    names_together.append(str(names))
                print(", ".join(names_together))
                print('\n')
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
                count_exp = 0
                count_inexp = 0
                for player in Warriors:
                    if player['experience'] == True:
                        count_exp += 1
                    else:
                        count_inexp += 1
                print('Total experienced: {}'.format(count_exp))
                print('Total inexperienced: {}'.format(count_inexp))
                a_h = average_height(Warriors)
                print('Average height: {}'.format(a_h))
                print("Players on Team: ")
                names_together =  []
                for player in Warriors:
                    names = player['name']
                    names_together.append(str(names))
                print("  " ", ".join(names_together))
                print('Guardians: ')
                names_together =  []
                for player in Warriors:
                    names = player['name']
                    names_together.append(str(names))
                print(", ".join(names_together))
                print('\n')
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

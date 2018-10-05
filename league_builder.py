import csv

experienced_players = []
inexperienced_players = []
sharks = []
raptors = []
dragons = []

def read_csv():
    with open("soccer_players.csv") as csv_file:
        players_reader = csv.reader(csv_file, delimiter=",")
        rows = list(players_reader)
        counter = 0
        for row in rows:
            if counter == 0:
                print(', '.join(row))
                counter += 1
            elif row[2] == 'YES':
                experienced_players.append(row)
                counter += 1
            else:
                inexperienced_players.append(row)
                counter += 1
    
    create_teams()


def create_teams():
    print(len(experienced_players))
    print('-'* 40)
    print(len(inexperienced_players))


# TODO 
"""Create variables and programming logic to divide the 18 players into three teams: Sharks, Dragons and Raptors. 
Make sure the teams have the same number of players on them, and that the experience players are divided equally across the three teams."""

#TODO
"""Create a text file named teams.txt that includes the name of a team, followed by the players on that team. 
List all three teams and their players."""

#TODO
"""In the list of teams include the team name on one line, followed by a separate line for each player. Include the player's name, 
whether the player has experience playing soccer, and the player's guardian names. 
Separate each bit of player information by a comma."""


if __name__ == '__main__':
    read_csv()
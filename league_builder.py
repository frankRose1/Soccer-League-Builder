import csv
import os

experienced_players = []
inexperienced_players = []
sharks = []
raptors = []
dragons = []
number_of_teams = 3

def read_csv():
    """Reads in data from a csv file and sorts the players in to two difference lists based on experience level"""
    with open("soccer_players.csv") as csv_file:
        players_reader = csv.reader(csv_file, delimiter=",")
        rows = list(players_reader)
        counter = 0
        for row in rows:
            if counter == 0:
                counter += 1
            elif row[2] == 'YES':
                experienced_players.append(row)
                counter += 1
            else:
                inexperienced_players.append(row)
                counter += 1
    
    create_teams()


def create_teams():
    """Each team gets 6 players, with an even number of experienced players on each team."""
    total_players = len(experienced_players) + len(inexperienced_players)
    players_per_team = total_players / number_of_teams
    i = 0
    while i < players_per_team / 2:
        add_players_to_team(raptors)
        add_players_to_team(sharks)
        add_players_to_team(dragons)
        i += 1

    create_roster_file()


def add_players_to_team(team):
    """Takes the last player in the sorted lists and adds them to one of the 3 teams."""
    team.append(experienced_players.pop())
    team.append(inexperienced_players.pop())


def create_roster_file():
    """Create a text file named teams.txt that includes the name of a team, followed by the players on that team. 
        List all three teams and their players. Provide the player name, parent/gaurdian name, and if they are experienced.
        Also removes the teams.txt file if it already exists to start from scratch.
    """
    if os.path.exists('teams.txt'):
        os.remove('teams.txt')
    file = open('teams.txt', 'a')
    file.write(file_content(raptors, 'raptors'))
    file.write(file_content(sharks, 'sharks'))
    file.write(file_content(dragons, 'dragons'))


def file_content(team, team_name):
    """Loops over each team and creates the text to be written in the teams.txt file"""
    string = ''
    string += '{} \n'.format(team_name.upper())
    string += '-'*20
    string+= '\n'
    for player in team:
        string += '{}, {}, {} \n'.format(player[0], player[2], player[3])
    string += '\n \n \n'
    return string


if __name__ == '__main__':
    read_csv()
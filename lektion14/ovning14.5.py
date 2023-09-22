def make_list(teams_dict):
    result_list = []

    for team_name, team_data in teams_dict.items():
        team_info = {
            'country': team_name,
            'wins': team_data['wins'],
            'draws': team_data['draws'],
            'losses': team_data['losses'],
            'goals for': team_data['goals for'],
            'goals against': team_data['goals against']
        }
        result_list.append(team_info)

    return result_list


# befintliga dictionary med matchinformation
teams = {
    'Brazil': {'wins': 2, 'draws': 1, 'losses': 0, 'goals for': 5, 'goals against': 1},
    'Serbia': {'wins': 1, 'draws': 0, 'losses': 2, 'goals for': 2, 'goals against': 4}
}

# omvandla till lista
teams_list = make_list(teams)

# Skriv ut den resulterande listan
for team_info in teams_list:
    print(team_info)

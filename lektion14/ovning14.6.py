def calculate_goal_difference(team):
    return team['goals for'] - team['goals against']

def calculate_points(team):
    return (team['wins'] * 3) + team['draws']

def print_table(teams_list):
    # Skriv ut tabellens rubrik
    print("-" * 82)
    print("| # | Nation           | W | D | L | GF | GA | GD | P |")
    print("-" * 82)

    # Sortera lagen efter poäng i fallande ordning
    sorted_teams = sorted(teams_list, key=lambda x: (-calculate_points(x), -calculate_goal_difference(x)))

    # Loopa igenom och skriv ut varje lag
    for index, team in enumerate(sorted_teams, start=1):
        GD = calculate_goal_difference(team)
        P = calculate_points(team)
        print(f"| {index:2} | {team['country'][:15]:15} | {team['wins']:1} | {team['draws']:1} | {team['losses']:1} | {team['goals for']:2} | {team['goals against']:2} | {GD:2} | {P:2} |")

    # Skriv ut avslutningen av tabellen
    print("-" * 82)


teams = [
    {'country': 'Brazil', 'wins': 2, 'draws': 1, 'losses': 0, 'goals for': 5, 'goals against': 1},
    {'country': 'Serbia', 'wins': 1, 'draws': 0, 'losses': 2, 'goals for': 2, 'goals against': 4},
    {'country': 'Switzerland', 'wins': 1, 'draws': 2, 'losses': 0, 'goals for': 5, 'goals against': 4},
    {'country': 'Costa Rica', 'wins': 0, 'draws': 1, 'losses': 2, 'goals for': 2, 'goals against': 5}
]

# Anropa funktionen print_table för att skriva ut tabellen
print_table(teams)

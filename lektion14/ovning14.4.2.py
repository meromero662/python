# Definiera dictionaryn teams med lagstatistik
teams = {
    'Brazil': {'wins': 0, 'draws': 0, 'losses': 0, 'goals for': 0, 'goals against': 0},
    'Serbia': {'wins': 0, 'draws': 0, 'losses': 0, 'goals for': 0, 'goals against': 0},
    'Switzerland': {'wins': 0, 'draws': 0, 'losses': 0, 'goals for': 0, 'goals against': 0},
    'Costa Rica': {'wins': 0, 'draws': 0, 'losses': 0, 'goals for': 0, 'goals against': 0}
}


# Funktionen för att lägga till matchresultat
def add_game(home_team, home_score, away_team, away_score):
    # Uppdatera målstatistik för hemmalaget
    teams[home_team]['goals for'] += home_score
    teams[home_team]['goals against'] += away_score

    # Uppdatera målstatistik för bortalaget
    teams[away_team]['goals for'] += away_score
    teams[away_team]['goals against'] += home_score

    # Uppdatera vinster, förluster och oavgjorda
    outcome = 'draw' if home_score == away_score else ('win' if home_score > away_score else 'loss')

    if outcome not in teams[home_team]:
        teams[home_team][outcome] = 0
    if outcome not in teams[away_team]:
        teams[away_team][outcome] = 0

    teams[home_team][outcome] += 1
    teams[away_team][outcome] += 1


# Fyll teams med matchinformation
# 17 June 2018
add_game('Costa Rica', 0, 'Serbia', 1)
add_game('Brazil', 1, 'Switzerland', 1)

# 22 June 2018
add_game('Brazil', 2, 'Costa Rica', 0)
add_game('Serbia', 1, 'Switzerland', 2)

# 27 June 2018
add_game('Serbia', 0, 'Brazil', 2)
add_game('Switzerland', 2, 'Costa Rica', 2)

# Skriv ut resultatet
print("-------------------------------------")
print("| Nation      | W | D | L | GF | GA |")
print("-------------------------------------")
for team, stats in teams.items():
    print(
        f"| {team:12} | {stats.get('win', 0):1} | {stats.get('draw', 0):1} | {stats.get('loss', 0):1} | {stats['goals for']:2} | {stats['goals against']:2} |")

import random


class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def value(self):
        if self.rank in ['Kung', 'Dam', 'Knekt']:
            return 10
        elif self.rank == 'Ess':
            return [1, 14]  # Ess kan vara både 1 och 14

        return int(self.rank)

    def __str__(self):
        return f"{self.rank} av {self.suit}"


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw_card(self, deck):
        card = deck.pop()
        self.hand.append(card)

    def calculate_score(self):
        scores = [0]  # Start med en tom lista av poäng

        # Hitta alla ess i handen
        aces = [card for card in self.hand if card.rank == 'Ess']

        for card in self.hand:
            # Summera poängen för varje kort
            card_scores = []
            for score in scores:
                if card.rank == 'Ess':
                    card_scores.extend([score + 1, score + 14])  # Behandla Ess som både 1 och 14
                else:
                    card_scores.append(score + card.value())
            scores = card_scores

        # Välj det högsta poängvärdet som är mindre än eller lika med 21
        valid_scores = [score for score in scores if score <= 21]

        if valid_scores:
            return max(valid_scores)
        else:
            return min(scores)


def get_player_name(player_number):
    while True:
        name = input(f"Ange namn för spelare {player_number}: ")
        if name.strip():
            return name


def play_game():
    suits = ['Hjärter', 'Ruter', 'Spader', 'Klöver']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Knekt', 'Dam', 'Kung', 'Ess']
    deck = [Card(rank, suit) for suit in suits for rank in ranks]
    random.shuffle(deck)

    player_name = get_player_name(1)
    player = Player(player_name)

    computer = Player("Datorn")

    for _ in range(2):
        player.draw_card(deck)
        computer.draw_card(deck)

    while True:
        print(f"{player.name}:")
        for card in player.hand:
            print(card)
        user_input = input("Vill du dra ett kort till? (ja/nej): ").lower()
        if user_input == 'ja':
            player.draw_card(deck)
            user_score = player.calculate_score()
            if user_score > 21:
                print("Du förlorade! Datorn vinner.")
                return
        else:
            break

    while computer.calculate_score() < 17:
        computer.draw_card(deck)

    print("Datorn:")
    for card in computer.hand:
        print(card)

    user_score = player.calculate_score()
    computer_score = computer.calculate_score()

    if computer_score > 21 or (user_score <= 21 and user_score > computer_score):
        print(f"{player.name} vann!")
    elif user_score == computer_score:
        print("Det blev lika!")
    else:
        print("Datorn vann!")


if __name__ == "__main__":
    play_game()



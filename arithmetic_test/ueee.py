import random

users_name = input('Enter your name: ')
if users_name == "!done":
    print("Bye!")
    exit() #break нельзя использовать вне цикла
print(f'Hello {users_name}!')
basic_game_options = ['paper', 'rock', 'scissors', '!done'] #'lizard', 'spock',
players_chosen_options = []


def player_chosen_options():
    global players_chosen_options
    players_chosen_options = input('What options do you want to play with? Enter options separated by commas. If you want default, press Enter:').strip().split(',')
    if len(players_chosen_options) == True and players_chosen_options[0] == "!done":
        print("Bye!")
        exit()
    if not players_chosen_options[0]:
        players_chosen_options = basic_game_options[:-1]
    return players_chosen_options


def get_user_score(name, filename="rating.txt"):
    try:
        with open(filename, 'r') as file:
            for line in file:
                player, score = line.strip()
                if player == name:
                    return int(score)
    except FileNotFoundError:
        pass
    return 0


def update_user_score(name, score, filename="rating.txt"):
    scores = {}
    try:
        with open(filename, 'r') as file:
            for line in file:
                player, points = line.strip().split()
                scores[player] = int(points)
    except FileNotFoundError:
        pass
    scores[name] = score
    with open(filename, 'w') as file:
        for player, points in scores.items():
            file.write(f"{player} {points}\n")


def determine_winner(user_choice, computer_choice):
    winning_cases = {
        'rock': ['scissors', 'lizard'],
        'paper': ['rock', 'spock'],
        'scissors': ['paper', 'lizard'],
        'lizard': ['spock', 'paper'],
        'spock': ['scissors', 'rock']
    }
    if user_choice == computer_choice:
        return 'draw'
    elif computer_choice in winning_cases.get(user_choice, []):
        return "win"
    else:
        return "lose"


def gameplay():
    score = get_user_score(users_name)
    while True:
        users_option = input('Choose option: ').strip().lower()
        computer_chosen_option = random.choice(players_chosen_options)
        result = determine_winner(users_option, computer_chosen_option)
        if users_option == '!done':
            print(f'Bye! Your score is {score}')
            update_user_score(users_name, score)
            break
        if users_option not in players_chosen_options:
            print('Invalid input.')
            continue
        if result == "draw":
            print(f'Draw! Computer chose {computer_chosen_option}.')
            score += 50
        elif result == "win":
            print(f'You win! Computer chose {computer_chosen_option}.')
            score += 100
        else:
            print(f'You lost! Computer chose {computer_chosen_option}.')
        update_user_score(users_name, score)


player_chosen_options()
gameplay()
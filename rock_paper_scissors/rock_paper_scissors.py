import random


users_name = input('Enter your name: ')
if users_name == "!done":
    print("Bye!")
    exit() #break нельзя использовать вне цикла
print(f'Hello {users_name}!')
basic_game_options = ['paper', 'rock', 'scissors']
possible_game_options = ['paper', 'rock', 'scissors', 'lizard', 'spock', 'gun', 'lightning', 'devil', 'dragon', 'water', 'snake', 'fire', 'air', 'sponge', 'wolf', 'tree', 'human']


def player_chosen_options():
    while True:
        options = input('What options do you want to play with? Enter options separated by commas. If you want default, press Enter:').strip()
        if options == "!done":
            print('Bye!')
            exit()
        if not options:
            return basic_game_options
        options = [opt.strip().lower() for opt in options.split(',') if opt.strip()]
        if len(options) < 3:
            print('Invalid input. Enter at least three options!')
            continue
        return sorted(set(options))


def get_user_score(name, filename="rating.txt"):
    try:
        with open(filename, 'r') as file:
            for line in file:
                player, score = line.strip().split()
                if player == name:
                    return int(score)
    except (FileNotFoundError, ValueError):
        pass
    return 0


def update_user_score(name, score, filename="rating.txt"):
    scores = {}
    try:
        with open(filename, 'r') as file:
            for line in file:
                player, points = line.strip().split()
                scores[player] = int(points)
    except (FileNotFoundError, ValueError):
        pass
    scores[name] = score
    with open(filename, 'w') as file:
        for player, points in scores.items():
            file.write(f"{player} {points}\n")


def determine_winner(user_choice, computer_choice, choices):
    if user_choice == computer_choice:
        return 'draw'
    users_index = choices.index(user_choice)
    computers_index = choices.index(computer_choice)
    half = len(choices) // 2
    if(computers_index - users_index) % len(choices) <= half:
        return "win"
    else:
        return "lose"


def gameplay():
    players_chosen_options = player_chosen_options()
    score = get_user_score(users_name)
    while True:
        users_option = input('Choose option: ').strip().lower()
        if users_option == '!done':
            print(f'Bye! Your score is {score}')
            update_user_score(users_name, score)
            new_game_plus = input("Do you want to play again? (yes/no): ").strip().lower()
            if new_game_plus in ['yes', 'y']:
                gameplay()
            else:
                print('Bye!')
                exit()
        if users_option not in players_chosen_options:
            print(f'Invalid input. {users_option} not in game list')
            continue
        computer_chosen_option = random.choice(players_chosen_options)
        result = determine_winner(users_option, computer_chosen_option, players_chosen_options)
        if result == "draw":
            print(f'Draw! Computer chose {computer_chosen_option}.')
            score += 50
        elif result == "win":
            print(f'You win! Computer chose {computer_chosen_option}.')
            score += 100
        else:
            print(f'You lost! Computer chose {computer_chosen_option}.')
        update_user_score(users_name, score)


gameplay()

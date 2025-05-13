import random


def generate(level):
    if level == 1:
        number_1 = random.randint(2, 9)
        number_2 = random.randint(2, 9)
        operation = random.choice(['*', '-', '+'])
        example_1 = f'{number_1} {operation} {number_2}'
        return example_1, eval(example_1)


    elif level == 2:
        number = random.randint(11, 29)
        example_2 = f'{number}^2'
        return example_2, number**2


def test_running(level):
    correct_answers = 0
    for _ in range(5):
        question, correct_answer = generate(level)
        print(f'{question}')
        while True:
            try:
                answer = input('> ').strip()
                if answer.lstrip('-').isdigit():
                    if int(answer) == correct_answer:
                        print('Right!')
                        correct_answers += 1
                    else:
                        print('Wrong!')
                    break
                else:
                    print('Incorrect format. Please enter a valid number.')
            except ValueError:
                print('Incorrect format. Please enter a valid number.')
    print(f'Your mark is {correct_answers}/5.')
    return correct_answers


def save_results(correct_answers):
    while True:
        results = input('Would you like to save your result to a file? Enter yes or no: ').strip().lower()
        if results in ['yes', 'y']:
            u_name = input('Enter your name: ').strip()
            results_txt = f'{u_name}: your result is {correct_answers}/5.\n'
            with open('results.txt', 'a') as file:
                file.write(results_txt)
            print('Result saved!')
            break
        elif results in ['no', 'n']:
            break
        else:
            print('Invalid input. Please enter yes or no.')


def main():
    print('Hello, user!')
    while True:
        try:
            level = int(input('Choose difficulty mode:\n1 - Easy\n2 - Hard\n> ').strip())
            if level in [1, 2]:
                correct_answer = test_running(level)
                break
            else:
                print('Invalid input. Please enter 1 or 2.')
        except ValueError:
            print('Incorrect format.')


if __name__ == "__main__":
    main()

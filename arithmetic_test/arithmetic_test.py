import random
print('Hello user!')


while True:
    mode = input('What difficult mode you want:\nIf you want easy mode type 1\nIf you want hard mode type 2\n>')
    if mode == '1':
        operations = ['*', '-', '+']
        correct_answers = 0
        for _ in range(5):
            number_1 = random.randint(2, 9)
            number_2 = random.randint(2, 9)
            operation = random.choice(operations)
            example = f'{number_1}{operation}{number_2}'
            print(example)
            right_answer = eval(example)
            while True:
                try:
                    answer = int(input('>'))
                    if answer == right_answer:
                        print('Right!')
                        correct_answers += 1
                        break
                    else:
                        print('Wrong!')
                        break
                except ValueError:
                    print("Incorrect parameters")
            print(f'Your mark is {correct_answers}/5.')


    elif mode == '2':
        correct_answers = 0
        for _ in range(5):
            number = random.randint(11, 29)
            example = f'{number}**2'
            print(example)
            right_answer = number ** 2
            while True:
                answer = input('>')
                if answer.isdigit():
                    if int(answer) == right_answer:
                        print('Right!')
                        correct_answers += 1
                        break
                    else:
                        print('Wrong!')
                        break
                else:
                    print('Incorrect format.')
            print(f'Your mark is {correct_answers}/5.')


        results = input('Would you like to save your result to file? Enter yes or no\n>')
        if results.lower() in ['yes', 'y']:
            u_name = input('Put down your name:\n>')
            results_txt = f'{u_name}: your results is {correct_answers}/5.\n'
            with open('results.txt', 'a') as file:
                file.write(results_txt)
            print(results_txt)
            break
        else:
            break


    else:
        print("Invalid mode. Please enter 1 or 2.")
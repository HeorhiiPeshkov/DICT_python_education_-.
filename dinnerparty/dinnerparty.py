import random
friend_list = int(input('Enter the number of friends joining (including you):\n>'))
friend_name_list = []
if friend_list != 0:
    friend_list_number = {}
    for i in range(friend_list):
        friend_name = input(f'Enter the friend`s name\n>')
        friend_list_number[friend_name] = 0
        friend_name_list.append(friend_name)
    total_amount = input("Enter the total amount:\n> ")
    total_amount = float(total_amount)
    friend_amount = round(total_amount / friend_list, 2)
    for friend in friend_list_number:
        friend_list_number[friend] = friend_amount
    WIL = input('Do you want to use the "Who is lucky?" feature? Write Yes/No:\n>')
    if WIL == "Yes":
        lucky_one = random.choice(friend_name_list)
        print(f'{lucky_one} is lucky')
        friend_name_list.remove(lucky_one)
        friend_amount = round(total_amount / len(friend_name_list), 2)
        for friend in friend_name_list:
            friend_list_number[friend] = friend_amount
        friend_list_number[lucky_one] = 0
    else:
        print('No one is going to be lucky')
        friend_amount = round(total_amount / friend_list, 2)
        for friend in friend_list_number:
            friend_list_number[friend] = friend_amount
    print("Friends and their amounts:", friend_list_number)
else:
    print('No one is joining for the party')

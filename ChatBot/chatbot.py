botname = ('chatbot')
birthyear = ('2024')
print(f'Hello! My name is {botname}.\nI was created in {birthyear}.')

print('Please, remind me your name.')
yourname = input('>')
print(f'What a great name you have, {yourname}!')

print('Let me guess your age.\nEnter remainders of dividing your age by 3, 5 and 7.')
remainder3 = int(input('>'))
remainder5 = int(input('>'))
remainder7 = int(input('>'))
yourage = (remainder3 * 70 + remainder5 * 21 + remainder7 * 15) % 105
print(f'(Your age is {yourage}; thats a good time to start programming!)')

print('Now I will prove to you that I can count to any number you want.')
nyw = int(input('>'))
if nyw > 0:
    number = 0
    while number <= nyw:
        print(f'{number}!')
        number = number + 1

print("Who performs main character in Titanic?")
question = int(input("1. Robert De Niro.\n2. Leonardo Dicaprio.\n3. Johny Depp.\n4. Tom Hardy.\n>"))
while question == 2:
    print("Completed!")
    break
else:
    print("Please, try again.")
    question = int(input(">"))

print('Hello user! If you need help type !help. If you need to finish code type !done')

formatters = ["plain", "bold", "italic", "header", "link", "inline-code", "ordered-list", "unordered-list", "new-line"]
special_commands = ["!help", "!done"]
mct = ""

def plain(text):
    return text

def bold(text):
    return f"**{text}**"

def italic(text):
    return f"*{text}*"

def inline_code(text):
    return f"`{text}`"

def header(text, level):
    return f"\n{'#' * level} {text}\n" if 1 <= level <= 6 else ""

def link(label, url):
    return f"[{label}]({url})"

def ordered_list(items):
    return "\n" + "\n".join(f"{i + 1}. {item}" for i, item in enumerate(items)) + "\n"

def unordered_list(items):
    return "\n" + "\n".join(f"* {item}" for item in items) + "\n"

def show_help():
    print("Available formatters:", ", ".join(formatters))
    print("Special commands:", ", ".join(special_commands))

while True:
    chafo = input("Choose a formatter: ")
    if chafo in special_commands:
        if chafo == "!help":
            show_help()
        elif chafo == "!done":
            with open("output.md", "w") as file:
                file.write(mct)
            print(mct)
            break
    elif chafo in formatters:
        if chafo == 'plain':
            users_txt = input('Text: ')
            mct += "\n" + plain(users_txt)
        elif chafo == 'bold':
            users_txt = input('Text: ')
            mct += "\n" + bold(users_txt)
        elif chafo == 'italic':
            users_txt = input('Text: ')
            mct += "\n" + italic(users_txt)
        elif chafo == 'header':
            while True:
                try:
                    level = int(input('Level: '))
                    if 1 <= level <= 6:
                        break
                    else:
                        print("Level should be between 1 and 6.")
                except ValueError:
                    print("Invalid input. Please enter a number between 1 and 6.")
            users_txt = input('Text: ')
            mct += header(users_txt, level)
        elif chafo == 'link':
            label = input('Label: ')
            url = input('URL: ')
            mct += "\n" + link(label, url)
        elif chafo == 'inline-code':
            users_txt = input('Text: ')
            mct += "\n" + inline_code(users_txt)
        elif chafo == 'ordered-list':
            while True:
                try:
                    num_items = int(input('Number of rows: '))
                    if num_items > 0:
                        items = [input(f'Row #{i + 1}: ') for i in range(num_items)]
                        mct += ordered_list(items)
                        break
                    else:
                        print("The number of rows should be greater than zero.")
                except ValueError:
                    print("Invalid input. Please enter a number.")
        elif chafo == 'unordered-list':
            while True:
                try:
                    num_items = int(input('Number of rows: '))
                    if num_items > 0:
                        items = [input(f'Row #{i + 1}: ') for i in range(num_items)]
                        mct += unordered_list(items)
                        break
                    else:
                        print("The number of rows should be greater than zero.")
                except ValueError:
                    print("Invalid input. Please enter a number.")

        elif chafo == 'new-line':
            mct += "\n"
        print(mct)
    else:
        print("Unknown formatting type or command")

import os
import sys
import hashlib
import shutil


VCS_DIR = 'vcs'
CONFIG = VCS_DIR + '/config.txt'
INDEX = VCS_DIR  + '/index.txt'
LOG = VCS_DIR + '/log.txt'
COMMITS_DIR = VCS_DIR + '/commits'


commands = {
    'config': 'Make username.',
    'add': 'Add file',
    'commit': 'Commit changes',
    'log': 'Show log',
    'checkout': 'Return to one of the previous commits'
}


def init():
    os.makedirs(COMMITS_DIR, exist_ok=True)
    for file in [CONFIG, INDEX, LOG]:
        if not os.path.exists(file):
            open(file, 'w').close()


def read(path):
    if not os.path.exists(path):
        return ''
    with open(path, 'r') as f:
        return f.read().strip()


def write(path, text):
    with open(path, 'w') as f:
        f.write(text)


def append(path, text):
    with open(path, 'a') as f:
        f.write(text)


def get_username():
    return read(CONFIG)


def tracked_files():
    return read(INDEX).splitlines()


def file_hash(name):
    with open(name, 'rb') as f:
        return hashlib.sha1(f.read()).hexdigest()


def changes():
    if not os.path.getsize(LOG):
        return True
    files = tracked_files()
    last_commit = read(LOG).splitlines()[0].split()[1]
    for file in files:
        old_file = f'{COMMITS_DIR}/{last_commit}/{file}'
        if not os.path.exists(old_file) or file_hash(file) != file_hash(old_file):
            return True
    return False


def commit(message):
    if not message:
        print('Nothing to commit')
        return
    if not changes():
        print('Nothing to commit')
        return
    username = get_username()
    if not username:
        print('Type your username')
        return
    files = tracked_files()
    total_hash = ''.join([file_hash(file) for file in files])
    commit_user_id = hashlib.sha1(total_hash.encode()).hexdigest()
    commit_path = f'{COMMITS_DIR}/{commit_user_id}'
    os.makedirs(commit_path)
    for file in files:
        shutil.copy(file, f'{commit_path}/{file}')
    log_entry = f'commit {commit_user_id}\nAuthor: {username}\n{message}\n\n'
    write(LOG, log_entry + read(LOG))
    print('Changes are saved')


def show_log():
    log_text = read(LOG)
    if log_text:
        print(log_text)
    else:
        "There are no logs"


def checkout(commit_user_id):
    path = f'{COMMITS_DIR}/{commit_user_id}'
    if not os.path.exists(path):
        print('Commit not found')
        return
    for file in os.listdir(path):
        shutil.copy(f'{path}/{file}', file)
    print(f'Switched to commit {commit_user_id}')


def main():
    init()
    args = sys.argv[1:]
    if not args or args[0] == '--help':
        print('Here are commands:')
        for cmd, desc in commands.items():
            print(f'{cmd.ljust(10)}{desc}')
        return
    cmd = args[0]
    if cmd == 'config':
        if len(args) == 2:
            write(CONFIG, args[1])
            print(f'Username is {args[1]}')
        else:
            users_name = get_username()
            if users_name:
                print(users_name)
            else:
                print('Incorrect input!')
    elif cmd == 'add':
        if len(args) == 2:
            filename = args[1]
            if os.path.exists(filename):
                files = set(tracked_files())
                files.add(filename)
                write(INDEX, '\n'.join(files))
                print(f"There's {filename}")
            else:
                print(f"There's no {filename}")
        else:
            files = tracked_files()
            if files:
                print('Tracked files:')
                for file in files:
                    print(file)
            else:
                print('No files tracked.')
    elif cmd == 'commit':
        commit(args[1] if len(args) > 1 else '')
    elif cmd == 'log':
        show_log()
    elif cmd == 'checkout':
        if len(args) > 1:
            checkout(args[1])
        else:
            print('Type commit ID')
    else:
        print(f'{cmd} is unknown command')


if __name__ == '__main__':
    main()

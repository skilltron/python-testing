from pathlib import Path
filenames = ['cats.txt', 'dogs.txt']

for filename in filenames:
    try:
        path= Path(filename)
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        # print(f"Sorry the file: {path} is not available")
        pass
    else:
        for item in contents.splitlines():
            print(f'{item}')

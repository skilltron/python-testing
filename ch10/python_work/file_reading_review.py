# from pathlib import Path

# path = Path('pets.txt')
# contents = path.read_text()
# print(contents)

def readfile (path):
    from pathlib import Path
    path = Path(path)
    counter = 0
    try:
        contents = path.read_text().splitlines()
    except FileNotFoundError:
        print(f'File {path} is not present')
    else:
        for line in contents:
            counter += 1
            print(f'#{counter}: {line}')
    print(f' number of lines: {counter}')


readfile("colors.txt")
readfile("pets.txt")
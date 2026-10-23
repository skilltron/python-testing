from pathlib import Path
guests=""
path = Path('guest.txt')
while True:
    name = input("Enter your name (or 'q' to quit): ")
    if name == "q":
        path.write_text(guests)
        break
    else:
        guests = guests + (f'{name}\n')

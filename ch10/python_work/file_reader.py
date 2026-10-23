from pathlib import Path

path = Path('text_files/pi_digits.txt')
contents = path.read_text().rstrip()
print(contents)

path = Path('text_files/pi_digits.txt')
contents = path.read_text()
lines = contents.splitlines()
for line in lines:
    print(line)

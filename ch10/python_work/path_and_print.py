from pathlib import Path

def count_lines(path):
    path = Path(path)
    lines = path.read_text().splitlines()
    count = 0
    for line in lines:
        #print(line)
        count += 1
    return (count)

lines_counted = count_lines("dogs.txt")
print(lines_counted)

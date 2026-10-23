from pathlib import Path

path = Path('/Users/henryhaskell/python_testing/ch10/text_files/learning_python.txt')
print(path.read_text())

for line in path.read_text().splitlines():
    print (line.replace('Python', 'C'))

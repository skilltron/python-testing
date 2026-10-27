from pathlib import Path

mybooks = ["tdafotre.txt", "monte_cristo.txt"]
def frequency_count(books, word):
    """ Counts the freqency of a word in a text."""
    try:
        for book in books:
            print(f"This is my book {book}")
            count = book.line(word)
            print(f"The word {word} was found {count} number of times in {book}")
    except FileNotFoundError:
            print(f"Sorry {book} is not found.")
              

frequency_count(mybooks, "ran")

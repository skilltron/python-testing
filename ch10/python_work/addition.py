while True:
    first_number = input("first number:")
    second_number = input("second number:")
    try:
        total = int(first_number) + int(second_number)
    except ValueError:
        print('One entry is not a number, please try again.')
    else:
        print(total)
        break

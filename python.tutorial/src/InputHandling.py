while True:
    try:
        x = int(raw_input('Please enter a number: '))
        break
    except ValueError:
        print 'Oops! That was not a valid number. Try again...'
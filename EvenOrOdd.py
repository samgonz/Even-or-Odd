userNumber = input('Enter a whole number to find out if it is even or odd.\n')

def evenOrOddChecker():
    checkNumber = int(userNumber) % 2
    if checkNumber == 0:
        return 'even'
    else:
        return 'odd'

print(f'Congrats, the number {userNumber}, is {evenOrOddChecker()}!')
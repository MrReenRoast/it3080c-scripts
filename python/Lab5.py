import random

randomNumber = random.randint(1,10)
print("I'm thinking of a number between 1 and 10. Care to guess? (Type n to close)")
print(randomNumber)
myNumber = input()
while myNumber != 'n':
    try:
        myNumber = int(myNumber)
        if myNumber == randomNumber:
            print ('Wow, you guessed correctly! Would you like to try again?')
            randomNumber = random.randint(1,10)
            myNumber = input()
        elif myNumber > randomNumber and 1 <= myNumber <= 10:
            print('Too high!')
            myNumber = input()
        elif myNumber < randomNumber and 1 <= myNumber <= 10:
            print('Too low!')
            myNumber = input()
        else:
            print('That is not a valid input. Please specify a number between 1 and 10')
            myNumber = input()
    except ValueError:
        print('That is not a valid input. Please specify a number between 1 and 10')
        myNumber = input()


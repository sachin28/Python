import random

name = raw_input("Please Enter Your Name: ")

guessCount = 1
randomNumber = random.randint(1, 10)
print (randomNumber)

while guessCount < 10:

    guessedNumber = raw_input("Hello " + name + ", Please select a number between 1-10: ")

    if not (guessedNumber.isdigit() and 1 <= int(guessedNumber) <= 10):
        print("Enter a valid integer")

    else:
        guessedNumber = int(guessedNumber)

        if guessedNumber < randomNumber:
            print("You Entered a low value")

        elif guessedNumber > randomNumber:
            print("You entered a large value")

        elif guessedNumber == randomNumber:
            break

        else:
            print("something went wrong")

    guessCount = guessCount + 1

if guessedNumber == randomNumber:
    print("you guessed correct numer in " + str(guessCount) + " trial/s")

elif guessedNumber != randomNumber:
    print("You took " + str(guessCount) + " chances but could not answer, The answer is: " + str(randomNumber))

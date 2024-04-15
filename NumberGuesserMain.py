import random

def GuessNumber():
    start = int(input("Enter Starting Number: "))
    stop = int(input("Enter Last Number: "))

    if start > stop:
        print(f"The Start Number ({start}) can NOT be bigger than the Stop Number ({stop})!")
        return

    randomNumber = random.randrange(start, stop + 1)

    count = 0

    while True:
        userInput = int(input("Enter Your Guess: "))

        if userInput < start or userInput > stop:
            print(f"Your guess is not in the specified range! {start, stop}")
            continue

        if userInput == randomNumber: 
            count = count + 1
            print(f"You have Guessed the correct Number ({randomNumber}) in {count} tries!")
            break

        else:
            count = count + 1
            print(f"{userInput} is NOT the right guess!")

            ask = input("Would You like to try again? ")
            print()

            if ask.lower() in ["yes", "y"]:
                continue

            elif ask.lower() in ["no", "n"]:
                print()
                print(f"Attempts Taken: {count}")
                print(f"Number was: {randomNumber}")
                print()
                break

            else:
                print("Invalid Input!")
                break

GuessNumber()

import random

def GuessNumberEasy():
    print("> You are supposed to enter start and stop values and then try to guess the random number picked!")
    print("> You will be provided with hints at every input!")
    print("> Good Luck!")
    print()

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

            if userInput > randomNumber:
                print(f"Hint: Your Number ({userInput}) is larger than the random value!")
            else:
                print(f"Hint: Your Number ({userInput}) is smaller than the random value!")

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

def GuessNumberMedium():
    print("> You are supposed to enter start and stop values and then try to guess the random number picked!")
    start = int(input("Enter Starting Number: "))
    stop = int(input("Enter Last Number: "))

    if start > stop:
        print(f"The Start Number ({start}) can NOT be bigger than the Stop Number ({stop})!")
        return
    elif start == stop:
        print(f"The Start Number ({start}) can NOT be equal to the Stop Number ({stop})!")
        return
    
    totalHints = (start+stop)//4
    print(f"> You will be provided with {totalHints} hints!")
    print("> Good Luck!")
    print()


    randomNumber = random.randrange(start, stop + 1)

    count = 0
    while True:
        if totalHints > 0:
            askForHint = input(f"Would you like to use your hint right now? (Remaining Hints = {totalHints}) ")
        else:
            askForHint = "no"

        if askForHint.lower() in ["no", "n"]:
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
                    print(f"Hints Left: {totalHints}")
                    print(f"Number was: {randomNumber}")
                    print()
                    break

                else:
                    print("Invalid Input!")
                    break

        elif askForHint.lower() in ["yes", "y"]:
            totalHints = totalHints - 1
            userInput = int(input("Enter Your Guess: "))

            if userInput < start or userInput > stop:
                print(f"Your guess is not in the specified range! {start, stop}")
                continue

            if userInput == randomNumber: 
                count = count + 1
                print(f"You have Guessed the correct Number ({randomNumber}) in {count} tries! With {totalHints} left!")
                break

            else:
                count = count + 1
                print(f"{userInput} is NOT the right guess!")
                if userInput > randomNumber:
                    print(f"Hint: Your Number ({userInput}) is larger than the random value!")
                else:
                    print(f"Hint: Your Number ({userInput}) is smaller than the random value!")

                ask = input("Would You like to try again? ")
                print()

                if ask.lower() in ["yes", "y"]:
                    continue

                elif ask.lower() in ["no", "n"]:
                    print()
                    print(f"Attempts Taken: {count}")                 
                    print(f"Hints Left: {totalHints}")
                    print(f"Number was: {randomNumber}")
                    print()
                    break

                else:
                    print("Invalid Input!")
                    break

    return
                

def GuessNumberHard():
    print("> In this mode, you are supposed to enter start and stop values and then try to guess the random number picked!")
    print("> Good Luck!")
    print()
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


while True:
    print("------------------------------------")
    print("Welcome to the Number Guesser Game!")
    print("------------------------------------")
    print("1. Easy Difficulty")
    print("2. Medium Difficulty")
    print("3. Hard Difficulty")
    print("4. Exit")
    print("------------------------------------")
    askUser = int(input("Enter difficulty input (1/2/3/4): "))

    if askUser == int(1):
        GuessNumberEasy()
    elif askUser == int(2):
        GuessNumberMedium()
    elif askUser == int(3):
        GuessNumberHard()
    elif askUser == int(4):
        break
    else:
        print("Invalid Input!")
        continue

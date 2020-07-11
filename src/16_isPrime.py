import sys
import time
import math


def isValid(userInput):
    if (userInput.isdigit() and int(userInput) > 0):
        return int(userInput)
    else:
        return False


def isPrime(userInput):
    # run a loop from the first prime number (2) to userInput + 1 (to include it)
    if userInput == 1:
        return ("1 is not a prime number")
    if userInput == 2:
        return ("2 is a prime number")
    maxDivisor = math.floor(math.sqrt(userInput))

    for i in range(3, maxDivisor + 1, 2):
        if (userInput % i == 0):
            return (f"{userInput} is not a prime number.")
    return (f"{userInput} is a prime number")


userInput = sys.argv
start_time = time.time()

if (len(userInput) != 2):
    print(
        "\n*** Only one number required after `python3 16_isPrime.py [number] ***`\n")
elif (isValid(userInput[1])):
    print(isPrime(int(userInput[1])))
else:
    print(
        "\n*** Please follow this format `python3 16_isPrime.py [1 >= number]` ***\n")

print("--- %s seconds ---" % (time.time() - start_time))

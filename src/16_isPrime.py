import sys


def isValid(userInput):
    if (userInput.isdigit() and int(userInput) > 0):
        return int(userInput)
    else:
        return False


def isPrime(num):
    if (num is 1):
        return("\n*** 1 is not a prime number. ***\n")
    for i in range(2, num):
        if (num % 2 is 0):
            return(f"\n*** {num} is not a prime number. ***\n")
        elif (i % 2 != 0 and num % i is 0):
            return(f"\n*** {num} is not a prime number. ***\n")
    return (f"\n*** {num} is a prime number. ***\n")


userInput = sys.argv

if (len(userInput) != 2):
    print(
        "\n*** Only one number required after `python3 16_isPrime.py [number] ***`\n")
elif (isValid(userInput[1])):
    print(isPrime(int(userInput[1])))
else:
    print(
        "\n*** Please follow this format `python3 16_isPrime.py [1 >= number]` ***\n")

import sys
import time


start_time = time.time()


def isValid(userInput):
    if (userInput.isdigit() and int(userInput) > 0):
        return int(userInput)
    else:
        return False


def generateList(maxNumber):
    # The algorithm of sieve of eratosthenes
    primes = []
    # create a list of 1 from 0 to userInput
    for i in range(maxNumber + 1):
        primes.append(1)
    # the value 1 represents prime and 0 not prime
    # 0 and 1 are not prime numbers
    primes[0] = 0
    primes[1] = 0
    return primes


def isPrime(userInput, primes):
    # run a loop from the first prime number (2) to userInput + 1 (to include it)
    for i in range(2, userInput + 1):
        if (primes[i] == 1):
            # if value is 1 (prime)
            # run a second loop, starting from the prime value index doubled (i * 2)
            # and increment by the index value (i)
            for j in range(i * 2, userInput + 1, i):
                # every multiply of the that prime number is not prime
                # so update it's value to 0
                primes[j] = 0

    result = [i for i, p in enumerate(primes) if p == 1 and i == userInput]
    if (len(result)):
        return (f"\n*** {userInput} is a prime number. ***\n")
    else:
        return(f"\n*** {userInput} is not a prime number. ***\n")


userInput = sys.argv

if (len(userInput) != 2):
    print(
        "\n*** Only one number required after `python3 16_isPrime.py [number] ***`\n")
elif (isValid(userInput[1])):
    primes = generateList(int(userInput[1]))
    print(isPrime(int(userInput[1]), primes))
else:
    print(
        "\n*** Please follow this format `python3 16_isPrime.py [1 >= number]` ***\n")

print("--- %s seconds ---" % (time.time() - start_time))

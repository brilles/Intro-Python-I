import sys

def isPrime(num):
    if int(num) > 0:
        num = int(num)
        numList = [i for i in range(2,num)]
        print(numList)
        for number in numList:
            if num % number == 0:
                return f"{num} is NOT prime, its divisible by (at least) {number}"
        else:
            return "its prime!"
    else: 
        return "Incorrect usage, number must be greater that 0"

print(isPrime(sys.argv[1]))
#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600_851_475_143 ?

#Min løsning No 1, dur ikke med store tal, løber tør for hukommelse
def findAllPossiblePrimes(number):
    
    primeList = [2,3]
    halfNumber = round(number/2)
    possiblePrimesForNumber =[]
        
    for i in range(1, halfNumber):
        if 6*i-1 <= halfNumber:
            primeList.append(6*i-1)
        else:
            break

        if 6*i+1<=halfNumber:
            primeList.append(6*i+1)
        else:
            break

    for num in primeList:
        if number % num == 0:
            possiblePrimesForNumber.append(num) 
    
    print(possiblePrimesForNumber)

    return possiblePrimesForNumber

def is_prime(number):
    halfNumber = round(number/2)

    for i in range(2, halfNumber):
        if number % i ==0:
            return False
    return True


def biggestPrime(primeList):

    for i in range(0, len(primeList)):
        if is_prime(primeList[len(primeList)-i-1]):
            return primeList[len(primeList)-i-1]
    
    return -1

print(biggestPrime(findAllPossiblePrimes(100)))


#Min løsning No 2, dur ikke med store tal, er ekstrem langsom
def findAllPossiblePrimes1(number):
    
    primeList = [2,3]
    halfNumber = round(number/2)
    possiblePrimesForNumber =[]
        
    for i in range(1, halfNumber):
        if 6*i-1 <= halfNumber:
             if is_prime1(6*i-1):
                primeList.append(6*i-1)
        else:
            break

        if 6*i+1<=halfNumber:
            if is_prime1(6*i+1):
                primeList.append(6*i+1)
        else:
            break

    for num in primeList:
        if number % num == 0:
            possiblePrimesForNumber.append(num) 
    
    print(possiblePrimesForNumber)

    return possiblePrimesForNumber

def is_prime1(number):
    halfNumber = round(number/2)

    for i in range(2, halfNumber):
        if number % i ==0:
            return False
    return True


def biggestPrime1(primeList):

    for i in range(0, len(primeList)):
        if is_prime1(primeList[len(primeList)-i-1]):
            return primeList[len(primeList)-i-1]
    
    return -1

print(biggestPrime1(findAllPossiblePrimes1(100)))

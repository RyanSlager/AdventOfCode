import math

def parseInput():
    inputFile = open("C:/Projects/AdventOfCode/Day One/D1_P1/input", "r")
    inputArray = inputFile.readlines()

    for x in range(len(inputArray)):
        inputArray[x] = int(inputArray[x].strip())

    return inputArray

def calculateFuel(module):
    moduleFuel = math.floor(module/3) - 2

    return moduleFuel

def main():
    moduleMassArray = parseInput()
    fuelArray = []

    for x in moduleMassArray:
        fuelArray.append(calculateFuel(x))

    print(sum(fuelArray))


if __name__ == "__main__":
    main()
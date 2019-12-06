import math

def parseInput():
    inputFile = open("C:/Projects/AdventOfCode/Day One/D1_P1/input", "r")
    inputArray = inputFile.readlines()

    for x in range(len(inputArray)):
        inputArray[x] = int(inputArray[x].strip())

    return inputArray

def calculateFuel(moduleMass):
    moduleFuel = math.floor(moduleMass/3) - 2
    totalFuel = moduleFuel

    if math.floor(moduleFuel/3) - 2 >= 0:
        totalFuel += calculateFuel(moduleFuel)

    return totalFuel

def main():
    moduleMassArray = parseInput()
    fuelArray = []

    for x in moduleMassArray:
        fuelArray.append(calculateFuel(x))

    print(sum(fuelArray))


if __name__ == "__main__":
    main()
def parseInput():
    inputFile = open("C:\Projects\AdventOfCode\Day Two\D2_P1\input", "r")
    inputString = inputFile.read()
    intcodeArray = inputString.split(",")

    for x in range(len(intcodeArray)):
        intcodeArray[x] = int(intcodeArray[x])

    return intcodeArray

def intcodeComputer(intcodeArray):
    x = 0
    y = 0
    z = 0
    for i in range(len(intcodeArray)):
        if i % 4 == 0:
            if intcodeArray[i] == 1:
                x = intcodeArray[i + 1]
                y = intcodeArray[i + 2]
                z = intcodeArray[i + 3]

                intcodeArray[z] = intcodeArray[x] + intcodeArray[y]

            elif intcodeArray[i] == 2:
                x = intcodeArray[i + 1]
                y = intcodeArray[i + 2]
                z = intcodeArray[i + 3]

                intcodeArray[z] = intcodeArray[x] * intcodeArray[y]

            elif intcodeArray[x] == 99:
                break

    return intcodeArray

def main():
    intcodeProg = parseInput()
    intcodeResult = intcodeComputer(intcodeProg)
    print(intcodeResult)


if __name__ == "__main__":
    main()

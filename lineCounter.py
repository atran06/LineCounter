import os

def validExt(filename, validExtentions):
    index = 0
    while filename[index : index + 1] != "." and index != len(filename):
        index += 1

    return (filename[index : len(filename)] in validExtentions)

def countLines(dir):
    counter = 0

    file = open(dir, errors = 'ignore').readlines()

    for _ in file:
        counter += 1

    return counter

def crawlDirectories(dir, total, validExtentions):
    for filename in os.listdir(dir):

        if os.path.isdir(dir + "\\" + filename): 
            crawlDirectories(dir + "\\" + filename, total, validExtentions)

        else:
            if(validExt(filename, validExtentions)):
                numLines = countLines(dir + "/" + filename) 
                print(filename + ": " + str(numLines) + " lines")
                total[0] = total[0] + numLines

def getExtentions(str):
    words = []

    lastIndex = 0
    
    for i in range(len(str)):
        if i == len(str) - 1: 
            words.append(str[lastIndex : len(str)].strip())

        elif str[i : i + 1] == ',':
            words.append(str[lastIndex : i].strip())
            lastIndex = i + 1

    return words

def countTotalLines(dir, validExtentions):
    total = [0]  
    crawlDirectories(dir, total, getExtentions(validExtentions))

    return total[0]     

def main():

    directory = input("Enter directory of files: ")
    validExtentions = input("Enter file extentions seperated by a comma: ")

    print("\nTotal: " + str(countTotalLines(directory, validExtentions)))

    input("Press any key to continue...")

if __name__ == "__main__":
    main()
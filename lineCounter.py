import os

def validExt(filename):

    validExtentions = [".java", ".py", ".cpp", ".h"]

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

def crawlDirectories(dir, total):
    for filename in os.listdir(dir):

        if os.path.isdir(dir + "\\" + filename): 
            crawlDirectories(dir + "\\" + filename, total)

        else:
            if(validExt(filename)):
                numLines = countLines(dir + "/" + filename) 
                print(filename + ": " + str(numLines) + " lines")
                total[0] = total[0] + numLines

def countTotalLines(dir):
    total = [0]  
    crawlDirectories(dir, total)

    return total[0]     

def main():

    directory = input("Enter directory of files: ")

    print("\nTotal: " + str(countTotalLines(directory)))

if __name__ == "__main__":
    main()
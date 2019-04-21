import os

def validExt(ext):

    validExtentions = [".java", ".py", ".cpp", ".h"]

    file = input("Enter a filename: ")

    index = 0
    while file[index : index + 1] != "." and index != len(file):
        index += 1

    return (file[index : len(file)] in validExtentions)

def main():

    counter = 0
    directory = input("Enter directory of files: ")

    for filename in os.listdir(directory):
        file = open(directory + "\\" + filename, "r").readlines()

        for _ in file:
            counter += 1

    print(counter)

if __name__ == "__main__":
    main()
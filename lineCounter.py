import os

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
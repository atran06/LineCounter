import os

# Function: validExt(filename, validExtentions)
# Desc: Checks a filename and returns whether or not it's a valid file based on the extention
# Params: filename - file name of the file to check
#         validExtentions - list of valid extentions to check against
def validExt(filename, validExtentions):
    index = 0
    # Increments index until the char at the index is a period or it reaches the end of the string
    while filename[index : index + 1] != "." and index != len(filename): 
        index += 1

    return (filename[index : len(filename)] in validExtentions)

# Function: countLines(dir)
# Desc: Counts how many lines are in a given file
def countLines(dir):
    counter = 0

    file = open(dir, errors = 'ignore').readlines() # reads lines of the file into a list

    for _ in file:
        counter += 1

    return counter

# Function: crawDirectories(dir, total, validExtentions)
# Desc: Recursively goes through every file in a directory and utilizes countLines() to return the total 
#       number of lines in the directory.
# Params: dir - the directory/folder to begin at
#         total - holds the total amouont of lines (using an array due to mutability)
#         validExtentions - a list of the valid extentions for counting lines
def crawlDirectories(dir, total, validExtentions):
    for filename in os.listdir(dir):

        if os.path.isdir(dir + "\\" + filename): # checks if filename is a folder
            crawlDirectories(dir + "\\" + filename, total, validExtentions)

        else:
            if(validExt(filename, validExtentions)): # if file is a valid file
                numLines = countLines(dir + "/" + filename) 
                print(filename + ": " + str(numLines) + " lines")
                total[0] = total[0] + numLines

# Function: getExtentions(str)
# Desc: Extracts extentions from a single string if they're seperated by a comma. Ex: ".py, .java, .cpp"
# Params: str - a string containing extentions seperated by a comma
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

# Function: countTotalLines(dir, validExtentions)
# Desc: A wrapper for the recursive function crawlDirectories()
# Params: dir - directory to begin counting lines
#         validExtentions - a string containing extentions seperated by a comma
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
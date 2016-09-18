def main():

    try:

        userfile=grabfile() #This calls the function responsibile for grabing the file from the user.

        readfile(userfile) # This is responsible for taking the contents of the file and storing it as a list.

    except AttributeError:

        print("You do not have access to the specified file")

        print("Please check with your system administrator")





def grabfile():

    ExitLoop=False

    while ExitLoop==False:

        try:

            pathfile=input("What is the path of your file?")

            # "C:/textfiles/sample.txt"

            file= open(pathfile,"r")

            return file

            #ExitLoop=True

        except FileNotFoundError:

            print("The file was not found, try again")



        except PermissionError:

            ExitLoop=True



def readfile(theFile):

    a = 0

    endofsentence = 0 #tracks the end of sentence delimeters

    report=theFile.read() #reads the list and stores it into a string named report

    count = len(report) # gets the length of report

    for a in range(0, count):

        if report[a] == '.' or report[a] == ',' or report[a] == '!' or report[a] == ';':

            endofsentence += 1 # increments sentence every time a delimeter is found

        else:
            endofsentence = 1
            print("Not a valid sentence")

    words = report.split() # create a list of words split on space

    print(words) # prints the list

    validwords = 0 # checks for valid words

    testword = 0

    b = 0

    for a in words: # cycle through word list looking for valid words

        testword = words[b]

        testword = len(testword)

        if testword >= 3:

            validwords += 1

        b += 1



    numberwords = len(words)

    print("The number of words is ", len(words))
    print("The total number of valid words is ", validwords)

    print("The total number of sentences is ", endofsentence)

    print("The average number of words per sentence is ", validwords / endofsentence)



main()








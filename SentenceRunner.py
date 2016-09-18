def main():
    try:
        userfile = grabfile()
        readfile(userfile)
    except AttributeError:
        print("You do not have permission to the specified file")
        print("Please check with your system administrator")


def grabfile():
    ExitLoop = False
    while ExitLoop == False:
        try:
            pathfile = input("Please input the path to your file: ")
            file = open(pathfile,"r")
            return file
        except FileNotFoundError:
            print("The file was not found. Try again")
        except PermissionError:
            ExitLoop = True
def readfile(thefile):
    a = 0
    endofsentence = 0
    report = thefile.read()
    count = len(report)
    for a in range(0, count):
        if report[a] == '.' or report[a] == ',' or report[a] == '!' or report[a] == ';' or report[a] == '?':
            endofsentence += 1
    sentence = report.split('.') # Attempting to have code not count extra '.' successively, but not able to figure what to do next!
    words = report.split()
    print(words)
    print(sentence)
    validwords = 0
    testword = 0
    b = 0
    for a in words:
        testword = words[b]
        testword = len(testword)
        if testword >= 3:
            validwords += 1
        b += 1


    numberwords = len(words)
    print("The total number of words in the report is:  ", len(words))
    print("The total number of valid words in the report is:  ", validwords)
    print("The average number of words per sentence is:  ", validwords / endofsentence)
    print("The total number of sentences: ", sentence) # pints sentences in a list
    # print(pathfile)
main()

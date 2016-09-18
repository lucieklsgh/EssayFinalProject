
'''
try:
    f=open("Test4.txt","r")
    r=open("C:/textfiles/sample.txt","r")
    t=open("C:/textfiles/third.txt","r")
    print(f.read(1))
    print(r.read(1))
    f.close()
except FileNotFoundError:
    print("Sorry Your File Was Not Found")
except PermissionError:
    print("You do Not Have Permission To Access The file")
'''
ValidInput=False
while ValidInput==False:
    try:
        #You may use these  2 lines or uncomment the fourth line.
        filename=input("Please Enter the Complete File Name ")
        f = open(filename, "r")
        #if you uncomment the following line then comment the 2 lines above
        #f=open(input("Please Enter the Complete File Name "),"r")
        print(f.read())
        ValidInput=True
        f.close()
    except FileNotFoundError:
        print("Sorry Your File Was Not Found, make sure you add the file extension (.txt)")
    except PermissionError:
        print("You do Not Have Permission To Access The file")

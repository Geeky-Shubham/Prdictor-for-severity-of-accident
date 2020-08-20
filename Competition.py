import os
print("do u want to run application or create a folder")
a = input()
if(("Create" in a) or ("create" in a)):
        print("enter name of ur folder")
        input(x)
        os.mkdir(x) #This will create folder in cureent working directory
else:
        print("We Will run Application for you just start interacting with us")
        while True:
            print("So What do you wanna run?")
            p = input()
            if (("run" in p) or ("execute" in p)) and ("chrome" in  p):
                os.system("chrome")
            if ("run" in p) and (("virtualbox" in p) or ("VirtualBox" in p) or ("VB" in p)):
                os.system("VirtualBox")
            if ("run" in p) and (("virtualbox" in p) or ("VirtualBox" in p) or ("VB" in p)):
                os.system("VirtualBox")
            elif ("exit" in p) or ("quit" in p):
                break

            else:
                print("Don't Support or Kindly! check the spelling again")

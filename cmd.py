#this can run batch files, too
#running "cmd" breaks the whole thing, however powershell command works.
#a few obscure commands don't work, and i can't be bothered to add support (prompt, doskey ect)
import os 
import sys
import platform
#all these packages should come in system

#open command window for authenticity if being run through an ide. may be commented out
if ("cmd" not in sys.argv):
    os.system("start /wait py cmd.py cmd")
    exit()

#this is entirely non-essential, it's just to add an authentic feel. edit at will. (to be clear this is the windows 10 header)
print(f"""Microsoft Windows [Version {platform.version()}]
Copyright (c) 2009 Microsoft Corporation. All rights reserved.
""")

#again, another authenticity addon.
os.system(f"title {os.getcwd()}")

while True:
    #get input
    command=input(f"{os.getcwd()}>")
    #cd handling since it doesn't work out the box
    if command[:2] == "cd" and len(command) > 2:
        try:
            os.chdir(command[3:])
            #change title to cwd
            os.system(f"title {os.getcwd()}")
            #create newline for visual clarity
            print("")
        #handle bad paths
        except:
            print(f"Path: {os.getcwd()}\\{command[3:]} Does not exist.\n")
            pass
    else:
        #run command
        os.system(command)
        #create newline for visual clarity
        print("")
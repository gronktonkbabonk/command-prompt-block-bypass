#this can run batch files, too
#running "cmd" breaks the whole thing, however powershell command works.
#a few obscure commands don't work, and i can't be bothered to add support (prompt, doskey ect)
import os 
import sys
import platform
import time
#all these packages should come in system

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
HOMEM = os.path.join(ROOT_DIR,"homemade")

for file in os.listdir(HOMEM):
    f = os.path.splitext(file)[-1].lower()
    if f != ".py" and f != ".bat":
        
        print("Invalid files in homemade folder. only .py and .bat files are currently supported.\n")
        while True:
            os.system("color 4")
            time.sleep(0.5)
            os.system("color f")
            time.sleep(0.5)

#open command window for authenticity if being run through an ide. may be commented out
# if ("cmd" not in sys.argv):
#     os.system("start /wait py cmd.py cmd")
#     exit()

#this is entirely non-essential, it's just to add an authentic feel. edit at will. (to be clear this is the windows 10 header)
print(f"""Microsoft Windows [Version {platform.version()}]
Copyright (c) 2009 Microsoft Corporation. All rights reserved.""")

#again, another authenticity addon.
os.system(f"title {os.getcwd()}")

while True:
    #detect if user tries to exit out with ctrl+C
    try:
        command=input(f"\n{os.getcwd()}>")
    
        #cd handling since it doesn't work out the box
        if command[:2] == "cd" and len(command) > 2:
            try:
                os.chdir(command[3:])
                #change title to cwd
                os.system(f"title {os.getcwd()}")
                #create newline for visual clarity
            #handle bad paths
            except:
                print(f"Path: {os.getcwd()}\\{command[3:]} Does not exist.\n")
                pass
        else:
            #run command
            run = os.system(f"{command} 2> nul")
            if run != 0:
                
                splitCommand = command.split(" ", 1)
                orgCommand = splitCommand[0]
                orgArgs = ""
                if len(splitCommand) == 2:
                    orgArgs = splitCommand[1]
                
                found = False
                suffix = ""
                for file in os.listdir(HOMEM):
                    f,suff = os.path.splitext(file)
                    f=f.lower()
                    suff=suff.lower()
                    if (f==orgCommand):
                        found = True
                        break
                if found and suff == ".py":
                    os.system(f"py {HOMEM}/{orgCommand}.py {orgArgs}")
                elif found and suff == ".bat":
                    os.system(f"{HOMEM}/{orgCommand} {orgArgs}")
                else:
                    os.system(command)
    except KeyboardInterrupt:
        print("")
        continue
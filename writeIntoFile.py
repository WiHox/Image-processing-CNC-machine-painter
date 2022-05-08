import time
from tkinter import filedialog, messagebox

from GCode import generateGCode


def generateCommandFile(UserInputObj):
    
    testCorrectInput(UserInputObj)
    nameOfTheFileToWriteIn = generateFileName()
    f = open(nameOfTheFileToWriteIn, "a+")
    
    generatedGCode = generateGCode(UserInputObj)
    f.write(generatedGCode)
    f.close()

    messagebox.showinfo("Success", "Fisierul a fost salvat")
    return 


def testCorrectInput(UserInputObj):
    errorCode = 4
    if errorCode == 1000:
        messagebox.showinfo("Error", "Not saved because something is missing")
    return 


def generateFileName():
    nameOfTheFile = "//FisierVopsire-" + time.strftime("%Y-%m-%d-%H-%M-%S") + ".txt"
    path = filedialog.askdirectory(initialdir="/", title="Select file")
    nameOfTheFileToWriteIn = path + nameOfTheFile
    return nameOfTheFileToWriteIn


#G01 Move x y z f
#G00 rapid move 
#G21 milimeters 
#G28 return home 
#M00 – Program stop

import time
from tkinter import filedialog, messagebox

from GCode import generateGCode
from inputObj import UserInput


def generateCommandFile(stCornerEntry, ndCornerEntry, rdCornerEntry, thCornerEntry, depthEntry, pauseEntry, pasEntry, vitezaEntry, distantaVopsireEntry):
    
    
    dateUser = UserInput(stCornerEntry.get(), ndCornerEntry.get(), rdCornerEntry.get(), thCornerEntry.get(), depthEntry.get(), pauseEntry.get(), pasEntry.get(), vitezaEntry.get(), distantaVopsireEntry.get())
    testCorrectInput(dateUser)
    nameOfTheFileToWriteIn = generateFileName()
    f = open(nameOfTheFileToWriteIn, "a+")
    
    generateGCode(dateUser, f)
    f.close()

    messagebox.showinfo("Success", "Fisierul a fost salvat")
    return 


def testCorrectInput(UserInputObj):
    errorCode = 4
    if errorCode == 1000:
        messagebox.showinfo("Error", "Not saved because something is missing")
    return 


def generateFileName():
    nameOfTheFile = "//FisierVopsire-" + time.strftime("%Y-%m-%d-%H-%M-%S") + ".tap"
    path = filedialog.askdirectory(initialdir="/", title="Select file")
    nameOfTheFileToWriteIn = path + nameOfTheFile
    return nameOfTheFileToWriteIn

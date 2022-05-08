from sqlite3 import Row
from tkinter import filedialog
from tkinter.filedialog import SaveAs
from tkinter.tix import COLUMN
import cv2 as cv

from cv2 import ROTATE_90_COUNTERCLOCKWISE
import numpy as np 
import tkinter as tk
from tkinter import *
from PIL import Image,ImageTk
from furnitureContour import getBiggestContour
from inputObj import UserInput
from setPicturePathAndNaming import setPath
from writeIntoFile import generateCommandFile

#I am setting here the path for the picture
nameOfFile, pathToImage = setPath()

#Constants
realityToPixelsRatioX = 1.37
realityToPixelsRatioY = 1.47
constantHeight = 4
inaltimeMasa = -328

#This method gets the picture of the object and returns the image and the boxing
def takePictureAndReturnCoordinates():
    cam_port = 0
    cam = cv.VideoCapture(cam_port)
    #result, image = cam.read()
    image = cv.imread(nameOfFile)
    image = cv.rotate(image, rotateCode=ROTATE_90_COUNTERCLOCKWISE)
    cv.imwrite(nameOfFile, image)

    box = getBiggestContour(image)

    image = cv.resize(image, [393,700], interpolation = cv.INTER_AREA)
    
    cv.imshow("sorin", image)
    cv.waitKey(0)
    cv.imwrite(nameOfFile, image)
    return box


def openPic(label, stCornerEntry, ndCornerEntry, rdCornerEntry, thCornerEntry):
    box = takePictureAndReturnCoordinates()
    myPictureWithContour = ImageTk.PhotoImage(Image.open(pathToImage))
    label.configure(image=myPictureWithContour)
    label.image = myPictureWithContour
    
    x,y = box[0]
    stCornerEntry.delete(0,END)
    stCornerEntry.insert(0, str(x) + ',' + str(y))

    x,y = box[1]
    ndCornerEntry.delete(0,END)
    ndCornerEntry.insert(0, str(x) + ',' + str(y))

    x,y = box[3]
    rdCornerEntry.delete(0,END)
    rdCornerEntry.insert(0, str(x) + ',' + str(y))

    x,y = box[2]
    thCornerEntry.delete(0,END)
    thCornerEntry.insert(0, str(x) + ',' + str(y))
    return

def calculateWithRatio(box):
    for i in range(4):
        box[i][0][0] *= realityToPixelsRatioX
        box[i][0][1] *= realityToPixelsRatioY
        temp =  box[i][0][0]
        box[i][0][0] = box[i][0][1]
        box[i][0][1] = temp

    return box

  
#Starts the GUI of the app
def startGUI():
    win = tk.Tk()
    win.title("Vopsitorie")
    win.geometry("1200x800")
    win.resizable(False, False)
    frame  = tk.Frame(win, width=1200, height=800)
    frame.pack()
    frame.place(anchor='e', relx=0.4, rely=0.5)
    box = takePictureAndReturnCoordinates()
    box = calculateWithRatio(box)
    myPictureWithContour = ImageTk.PhotoImage(Image.open(pathToImage))

    label = Label(frame, image = myPictureWithContour)
    
    label.pack()

    #Labels for the points of the furniture
    stCorner = tk.Label(win,text ='NV:', font='Helvetica 12 bold')
    stCorner.place(anchor=N, relx=0.55, rely=0.2)

    stCornerEntry = tk.Entry(win, width=10, bg='grey')
    x,y = box[0][0]
    stCornerEntry.insert(0, str(x) + ',' + str(y))
    stCornerEntry.place(anchor=N, relx=0.6, rely=0.203)

    ndCorner = tk.Label(win,text ='NE:', font='Helvetica 12 bold')
    ndCorner.place(anchor=N, relx=0.75, rely=0.2)

    ndCornerEntry = tk.Entry(win, width=10, bg='grey')
    x,y = box[3][0]
    ndCornerEntry.insert(-1, str(x) + ',' + str(y))
    ndCornerEntry.place(anchor=N, relx=0.8, rely=0.203)


    rdCorner = tk.Label(win,text ='SE:', font='Helvetica 12 bold') 
    rdCorner.place(anchor=N, relx=0.75, rely=0.3) 

    rdCornerEntry = tk.Entry(win, width=10, bg='grey')
    x,y = box[1][0]
    rdCornerEntry.insert(-1, str(x) + ',' + str(y))
    rdCornerEntry.place(anchor=N, relx=0.6, rely=0.303)


    
    thCorner = tk.Label(win,text ='SV:', font='Helvetica 12 bold')
    thCorner.place(anchor=N, relx=0.55, rely=0.3)

    thCornerEntry = tk.Entry(win, width=10, bg='grey')
    x,y = box[2][0]
    thCornerEntry.insert(-1, str(x) + ',' + str(y))
    thCornerEntry.place(anchor=N, relx=0.8, rely=0.303)


    depth = tk.Label(win,text ='Grosime:', font='Helvetica 12 bold', justify=LEFT)
    depth.place(anchor=N, relx=0.55, rely=0.4)

    depthEntry = tk.Entry(win, width=20, bg='white')
    depthEntry.place(anchor=N, relx=0.65, rely=0.403)
    depthEntry.insert(-1, 15)

    inCM = tk.Label(win,text ='in milimetrii', font='Helvetica 8 bold')
    inCM.place(anchor=N, relx=0.75, rely=0.4)


    pause = tk.Label(win,text ='Pauza:', font='Helvetica 12 bold', justify=LEFT)
    pause.place(anchor=N, relx=0.55, rely=0.5)

    pauseEntry = tk.Entry(win, width=20, bg='white')
    pauseEntry.place(anchor=N, relx=0.65, rely=0.503)
    pauseEntry.insert(-1, 15)

    inSeconds = tk.Label(win,text ='in secunde', font='Helvetica 8 bold')
    inSeconds.place(anchor=N, relx=0.75, rely=0.5)

    pas = tk.Label(win,text ='Pas sarpe:', font='Helvetica 12 bold', justify=LEFT)
    pas.place(anchor=N, relx=0.55, rely=0.6)

    pasEntry = tk.Entry(win, width=20, bg='white')
    pasEntry.place(anchor=N, relx=0.65, rely=0.604)
    pasEntry.insert(-1, 10)

    inCM2 = tk.Label(win,text =' in centrimetri', font='Helvetica 8 bold')
    inCM2.place(anchor=N, relx=0.75, rely=0.6)


    viteza = tk.Label(win,text ='Viteza:', font='Helvetica 12 bold', justify=LEFT)
    viteza.place(anchor=N, relx=0.55, rely=0.7)
   

    vitezaEntry = tk.Entry(win, width=20, bg='white')
    vitezaEntry.place(anchor=N, relx=0.65, rely=0.704)
    vitezaEntry.insert(-1, 500)

    ms = tk.Label(win,text =' in milimetrii pe minut', font='Helvetica 8 bold')
    ms.place(anchor=N, relx=0.765, rely=0.7)

    B = tk.Button(win, text ="Re-Photo", command = lambda:openPic(label, stCornerEntry, ndCornerEntry, rdCornerEntry, thCornerEntry))
    B.place(x=200,y=760,width=100,height=25)

    #Initializare obiect rdCornerEntry

    dateUser = UserInput(stCornerEntry.get(), ndCornerEntry.get(), rdCornerEntry.get(), thCornerEntry.get(), depthEntry.get(), pauseEntry.get(), pasEntry.get(), vitezaEntry.get())

    B = tk.Button(win, text ="Genereaza fisier comanda", command = lambda:generateCommandFile(dateUser))
    B.place(x=750,y=730,width=150,height=30)

    win.mainloop()
   

startGUI()

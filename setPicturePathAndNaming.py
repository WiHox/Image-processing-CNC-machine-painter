from datetime import date, datetime
import os

def setPath(): 
    #This has to be setup before putting it on another pc 
    path_to_file = "C:\\pozeAplicatie"
    if not os.path.exists(path_to_file):
        os.mkdir(path_to_file)
    rootDir = "C:\\Users\\Razvan Wiho\\poze\\"
    #os.chdir(rootDir)
    #today = date.today()
    #now = datetime.now()
    #d2 = today.strftime("%b-%d-%Y") + str(now.second)
    #nameOfFile = d2 + ".png"
    #pathToImage = rootDir + nameOfFile
    nameOfFile = "C:\\Users\\Razvan Wiho\\EdgeDetectionCNCMachinePainting\\poze\\Piesa1\\pozaTest1.jpg"
    return nameOfFile, nameOfFile
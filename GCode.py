

from typing import NewType


def generateGCode(userInputObj):

    #init values needed
    #parse the strings that are coming 
    splited = userInputObj.NV.split(",")
    NVX = float(splited[0])
    NVY = float(splited[1])

    splited1 = userInputObj.NE.split(",")
    NEX = float(splited1[0])
    NEY = float(splited1[1])

    splited2 = userInputObj.SE.split(",")
    SEX = float(splited2[0])
    SEY = float(splited2[1])
    
    splited3 = userInputObj.SV.split(",")
    SVX = float(splited3[0])
    SVY = float(splited3[1])

    
    Z = float(userInputObj.grosime)
    pauz = float(userInputObj.pauza)
    step = float(userInputObj.pas)
    speed = float(userInputObj.viteza)

    print(userInputObj)
    print("\n")
    print(NVX," ",NVY," ",NEX," ",NEY," ",SEX," ",SEY," ",SVX," ",SVY," ",Z," ",pauz," ",step," ",speed)
   
    return str(userInputObj.NE[0]) + str(userInputObj.NV[1])



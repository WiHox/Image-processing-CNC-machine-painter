from typing import NewType
zMasa = -325

def generateGCode(userInputObj, f):

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
    step = float(userInputObj.pas) * 10
    speed = int(userInputObj.viteza)
    grosime = int(userInputObj.grosime)
    distantaVopsire = int(userInputObj.distantaVopsire) * 10 

    vopsireSarpe = zMasa + distantaVopsire + grosime

    #inceput de program
    f.write("G90G80G21G49 \n")
    f.write("S15000 \n")

    #Sarpe X
    f.write("\n")
    f.write("(Sarpe pe X lung)\n")
    f.write("G0 X{NVX} Y{NVY} Z{Z} A0 B90 \n".format(NVX=NVX, NVY = NVY, Z=vopsireSarpe))
    f.write("G1 F{SPEED}\n".format(SPEED=speed))
    f.write("M3 \n")
    NVXCOPY = NVX
    SVXCOPY = SVX
    NVYCOPY = NVY + step
    f.write("G1 X{SVX}\n Y{NVY}\n".format(SVX=SVX, NVY = NVYCOPY))
    while NVYCOPY < NEY: 
        NVYCOPY = NVYCOPY + step
        f.write("X{NVXCOPY}\n Y{NVYCOPY}\n".format(NVXCOPY=NVXCOPY, NVYCOPY=NVYCOPY))
        temp = NVXCOPY
        NVXCOPY = SVXCOPY
        SVXCOPY = temp

    f.write("M5 \n")

    #Sarpe Y
    f.write("\n")
    f.write("(Sarpe pe Y lat )\n")
    f.write("G0 X{NVX} Y{NVY} Z{Z} A90 \n".format(NVX=NVX, NVY = NVY, Z=vopsireSarpe))
    f.write("G1 F{SPEED}\n".format(SPEED=speed))
    f.write("M3 \n")
    NVYCOPY = NVY
    NEYCOPY = NEY
    NVXCOPY = NVX + step
    f.write("G1 Y{NEY}\n X{NVX}\n".format(NEY=NEY, NVX=NVXCOPY))
    while NVXCOPY < SVX: 
        NVXCOPY = NVXCOPY + step
        f.write("Y{NVYCOPY}\n X{NVXCOPY}\n".format(NVYCOPY=NVYCOPY, NVXCOPY=NVXCOPY))
        temp = NVYCOPY
        NVYCOPY = NEYCOPY
        NEYCOPY = temp

    f.write("M5 \n")


    



   
    print(NVX," ",NVY," ",NEX," ",NEY," ",SEX," ",SEY," ",SVX," ",SVY," ",Z," ",pauz," ",step," ",speed, " ", distantaVopsire)











   
    return str(userInputObj.NE[0]) + str(userInputObj.NV[1])



#G01 Move x y z f
#G00 rapid move 
#G21 milimeters 
#G28 return home 
#M00 – Program stop



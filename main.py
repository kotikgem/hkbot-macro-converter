import os
import time
import gd
import json

print("Welcome to macro converter for hkbor by KotikGem v0.3")

typem = input("Please write the type of macro (tasbot/echo/hkcb(reverse converting not supported now))(2p are not supported now): ")

# if typem == "ddhor":

    # namemacro = input("Please write ddhor macro(now converter support only framemode macro): ")
    # namemacroout = input("Please write name of output file: ")

    # fm = open(namemacro, 'r')
    # fmout = open(namemacroout, 'a')

    # datta = json.loads(fm.read())

    # fps = datta['fps']
    # typemacro = datta['macro']

    # fmout.write(str(fps) + "\n")

    # #if "x-position" in typemacro:
       # # fmout.write("xposmode\n")

    # actions1p = datta['inputsP1']

    # i = 0
    # i2 = 0

    # while i != len(actions1p):
        # pos = actions1p[i]['position']
        # action = actions1p[i]['action']
        # fmout.write(str(pos) + "\n")
        # i += 1


    # fmout.write("end")

    # fm.close()
    # fmout.close()

    # print("Macros convertion has been succesfully!")
if typem == "tasbot":

    namemacro = input("Please write tasbot macro(now converter support only framemode macro): ")
    namemacroout = input("Please write name of output file: ")

    fm = open(namemacro, 'r')
    print(namemacro)
    fmout = open(namemacroout, 'a')
    print(namemacroout)

    datta = json.loads(fm.read())
    
    print(datta)

    fps = datta['fps']
    macro = datta['macro']

    fmout.write(str(fps) + "\n")
    fmout.write("framemode\n")

    #if "x-position" in typemacro:
       # fmout.write("xposmode\n")

    i = 0
    i2 = 0
    print("preparating to converting...")
    print(len(macro))
    
    ispress = False
    ispress2 = True

    while i != len(macro):
        if int(macro[i]['frame']) == 0:
            i += 1
            continue
        frm = macro[i]['frame']
        state_temp = macro[i]['player_1']['click']
        #action = actions1p[i]['action']
        if state_temp == 1:
            fmout.write(str(frm) + "\n")
        if state_temp == 2:
            fmout.write(str(frm) + "\n")
        #fmout.write(str(frm) + "\n")
        print(i)
        i += 1


    fmout.write("end")

    fm.close()
    fmout.close()

    print("Macros convertion has been succesfully!")

if typem == "echo":

    namemacro = input("Please write echo macro(now converter support only framemode macro for echo): ")
    namemacroout = input("Please write name of output file: ")

    fm = open(namemacro, 'r')
    fmout = open(namemacroout, 'a')

    datta = json.loads(fm.read())

    fps = datta['FPS']
    #typemacro = datta['Type']

    fmout.write(str(fps) + "\n")

    #if "Frames" in typemacro:
    fmout.write("framemode\n")

    actions = datta['Echo Replay']

    i = 0
    i2 = 0

    ispress = False
    ispress2 = True

    while i != len(actions):
        frame = actions[i]['Frame']
        action = actions[i]['Hold']
        if action == True and ispress2 == True:
            fmout.write(str(frame) + "\n")
            ispress = True
            ispress2 = False
        if action == False and ispress == True:
            fmout.write(str(frame) + "\n")
            ispress = False
            ispress2 = True
        i += 1


    fmout.write("end")

    fm.close()
    fmout.close()

    print("Macros convertion has been succesfully!")
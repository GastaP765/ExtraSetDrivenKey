import maya.cmds as mc
import UI

def develop():
    reload(UI)

def execution():
    develop()
    b = UI.DrvClass()
    b.mainWin()

def consoleKey():
    execution()

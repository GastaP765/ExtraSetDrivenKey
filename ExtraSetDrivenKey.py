import maya.cmds as mc
import UI
import setKey
import mirrorKey
import checkAttr
import mirrorCheck


def develop():
    reload(UI)
    reload(setKey)
    reload(mirrorKey)
    reload(checkAttr)
    reload(mirrorCheck)

def execution():
    develop()
    b = UI.DrvClass()
    b.mainWin()

def consoleKey():
    execution()

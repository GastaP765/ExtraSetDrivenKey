import maya.cmds as mc
import UI

def setKey(*args):
    drv = args[0]
    vat = args[1]
    drn = args[2]
    nat = args[3]

    for i in nat:
        mc.setDrivenKeyframe('{0}.{1}'.format(drn[0], i), cd='{0}.{1}'.format(drv[0], vat[0]))

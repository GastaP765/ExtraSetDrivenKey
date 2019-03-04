import maya.cmds as mc
import checkAttr
import mirrorCheck
import mirrorKey
import setKey

class DrvClass(object):
    def __init__(self):
        self.ts1 = ''
        self.ts2 = ''
        self.ts3 = ''
        self.ts4 = ''
        self.ts5 = ''
        self.ts6 = ''
        self.ts7 = ''
        self.ts8 = ''
        self.attr = []
        self.orgdrvn = ''
        self.orglst = ''
        self.mirror = ''
        self.defkey = ''

    def develop(self, *args):
        reload(checkAttr)
        reload(mirrorCheck)
        reload(mirrorKey)
        reload(setKey)

    def setKey(self, *args):
        drv = mc.textScrollList('ts1', q=True, si=True)
        vat = mc.textScrollList('ts2', q=True, si=True)
        drn = mc.textScrollList('ts3', q=True, si=True)
        nat = mc.textScrollList('ts4', q=True, si=True)
        setKey.setKey(drv, vat, drn, nat)

    def roadDriver(self, *args):
        slc = mc.ls(sl=True)
        mc.textScrollList('ts1', e=True, ra=True, append=slc)

    def driverAtt(self, *args):
        obj = mc.textScrollList('ts1', q=True, si=True)
        mc.select(obj)
        atr = mc.listAttr(obj, k=True)
        mc.textScrollList('ts2', e=True, ra=True, append=atr)

    def roadDriven(self, *args):
        slc = mc.ls(sl=True)
        mc.textScrollList('ts3', e=True, ra=True, append=slc)

    def drivenAtt(self, *args):
        obj = mc.textScrollList('ts3', q=True, si=True)
        mc.select(obj)
        atr = mc.listAttr(obj, k=True)
        mc.textScrollList('ts4', e=True, ra=True, append=atr)

    def orgSet(self, *args):
        slc = mc.ls(sl=True)
        mc.textField('tf1', e=True, tx=slc[0])
        checkAttr.attrGet()

    def orgAttr(self, *args):
        drvr = args[0]
        drvn = args[1]
        for i in range(len(drvr)):
            self.attr.append('{0} : {1}'.format(drvr[i], drvn[i]))

        mc.textScrollList('ts5', e=True, ra=True, append=self.attr)
        self.orgdrvn = mc.textField('tf1', q=True, tx=True)

        mirrorCheck.check(self.orgdrvn)
        self.mirSet()

    def mirSet(self, *args):
        slc = mc.ls(sl=True)
        mc.textField('tf2', e=True, tx=slc[0])
        self.orglst = mc.textScrollList('ts5', q=True, ai=True)
        mirrorCheck.check(self.orglst, 'mirSet')
    
    def mirlst(self, *args):
        a = args[0]
        mc.textScrollList('ts6', e=True, ra=True, append=a)

    def setDrvn(self, *args):
        org = mc.textScrollList('ts5', q=True, ai=True)
        tar = mc.textScrollList('ts6', q=True, ai=True)
        mirrorKey.preparation(org, tar)

    def close(self, *args):
        mc.deleteUI('DM')

    def mainWin(self, *args):
        if mc.window('DM', exists=True):
            mc.deleteUI('DM')

        win = mc.window('DM', t='Extra Set Driven Key', s=False, mxb=False, widthHeight=(395,520))
        mc.window('DM', e=True, widthHeight=(395,520))
        formt = mc.formLayout('formt')
        tabs = mc.tabLayout('tabs', w=145, h=20)
        
        form1 = mc.formLayout('form1')
        fr1 = mc.frameLayout('fr1', l='Driver', w=370, h=30)
        mc.setParent('..')
        ts1 = mc.textScrollList('ts1', w=175, h=175, sc=self.driverAtt)
        ts2 = mc.textScrollList('ts2', w=175, h=175)
        fr2 = mc.frameLayout('fr2', l='Driven', w=370, h=30)
        mc.setParent('..')
        ts3 = mc.textScrollList('ts3', w=175, h=175, sc=self.drivenAtt)
        ts4 = mc.textScrollList('ts4', ams=True, w=175, h=175)
        bt1 = mc.button(l='key', w=92, h=25, c=self.setKey)
        bt2 = mc.button(l='road Driver', w=92, h=25, c=self.roadDriver)
        bt3 = mc.button(l='road Driven', w=92, h=25, c=self.roadDriven)
        bt4 = mc.button(l='close', w=92, h=25, c=self.close)
        mc.setParent('..')

        form2 = mc.formLayout('form2')
        fr3 = mc.frameLayout('fr3', l='Original Driven', w=370, h=30)
        mc.setParent('..')
        tf1 = mc.textField('tf1', w=295, h=20)
        bt5 = mc.button(l='set', w=50, h=20, c=self.orgSet)
        ts5 = mc.textScrollList('ts5', ams=True, w=350, h=160)
        fr4 = mc.frameLayout('fr4', l='Mirror Driven', w=370, h=30)
        mc.setParent('..')
        tf2 = mc.textField('tf2', w=350, h=20)
        ts6 = mc.textScrollList('ts6', ams=True, w=350, h=160)
        bt7 = mc.button(l='mirror', w=184, h=25, c=self.setDrvn)
        bt8 = mc.button(l='close', w=184, h=25, c=self.close)        
        mc.setParent('..')

        mc.tabLayout(tabs, e=True, tl=((form1, 'Set'), (form2, 'Mirror')))

        mc.formLayout(formt, e=True, af=[
            (tabs, 'top', 0), (tabs, 'left', 0),
            (tabs, 'bottom', 0), (tabs, 'right', 0)
        ])
        mc.formLayout(form1, e=True, af=[
            (fr1, 'top', 10), (fr1, 'left', 10),
            (ts1, 'top', 50), (ts1, 'left', 20),
            (ts2, 'top', 50), (ts2, 'left', 195),
            (fr2, 'top', 235), (fr2, 'left', 10),
            (ts3, 'top', 275), (ts3, 'left', 20),
            (ts4, 'top', 275), (ts4, 'left', 195),
            (bt1, 'top', 465), (bt1, 'left', 10),
            (bt2, 'top', 465), (bt2, 'left', 103),
            (bt3, 'top', 465), (bt3, 'left', 196),
            (bt4, 'top', 465), (bt4, 'left', 289)
        ])
        mc.formLayout(form2, e=True, af=[
            (fr3, 'top', 10), (fr3, 'left', 10),
            (tf1, 'top', 40), (tf1, 'left', 20),
            (bt5, 'top', 40), (bt5, 'left', 320),
            (ts5, 'top', 65), (ts5, 'left', 20),
            (fr4, 'top', 235), (fr4, 'left', 10),
            (tf2, 'top', 265), (tf2, 'left', 20),
            (ts6, 'top', 290), (ts6, 'left', 20),
            (bt7, 'top', 465), (bt7, 'left', 10),
            (bt8, 'top', 465), (bt8, 'left', 196)
        ])
        mc.showWindow(win)

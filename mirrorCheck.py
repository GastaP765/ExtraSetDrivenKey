import maya.cmds as mc
import UI

def check(org='', key=''):
    con = []
    if type(org) is unicode:
        con.append(org)
    else:
        con = org
    res = []
    chk = 0
    alp = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    for i in con:
        x = '{}'.format(i)
        for f in alp:
            if '_{}L'.format(f) in '{}'.format(x) or '_{}R'.format(f) in '{}'.format(x):
                chk = 1
                if '_{}L'.format(f) in '{}'.format(x):
                    a = x.replace('_{}L'.format(f), '_{}R'.format(f))
                else:
                    a = x.replace('_{}R'.format(f), '_{}L'.format(f))
        if '_L' in '{}'.format(x) or '_R' in '{}'.format(x):
            chk = 1
            if '_L' in '{}'.format(x):
                a = x.replace('_L', '_R')
            else:
                a = x.replace('_R', '_L')
        elif 'L_' in '{}'.format(x) or 'R_' in '{}'.format(x):
            chk = 1
            if 'L_' in '{}'.format(x):
                a = x.replace('L_', 'R_')
            else:
                a = x.replace('R_', 'L_')
        res.append(a)
            
    if 'mirSet' == key:
        b = UI.DrvClass()
        b.mirlst(res)
    else:
        if chk == 1:
            mc.select(res[0])
        else:
            mc.select(cl=True)
        
    

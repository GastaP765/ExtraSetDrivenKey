import maya.cmds as mc
import UI

def preparation(*args):
    org = []
    tar = []
    Odrv = []
    Odrn = []
    Mdrv = []
    Mdrn = []

    if type(args[0]) is unicode:
        org.append(args[0])
    else:
        org = args[0]
    if type(args[1]) is unicode:
        tar.append(args[1])
    else:
        tar = args[1]
    
    for i in org:
        c = i.split(' : ')
        Odrv.append(c[0])
        Odrn.append(c[1])
    
    for i in tar:
        c = i.split(' : ')
        Mdrv.append(c[0])
        Mdrn.append(c[1])

    for i in range(len(Odrv)):
        a = mc.connectionInfo(Odrn[i], ged=True)
        flt = mc.keyframe(a, q=True, fc=True)
        val = mc.keyframe(a, q=True, vc=True)
        idx = mc.keyframe(a, q=True, iv=True)
        d = mc.keyTangent(a, q=True, itt=True)
        e = mc.keyTangent(a, q=True, ott=True)
        l = Mdrn[i]
        k = l.replace('.', '_')
        keep = mc.getAttr(Mdrv[i])
        chk = mc.connectionInfo(Mdrn[i], ied=True)
        if True is chk:
            mc.delete(k)

        for f in range(len(flt)):
            if 'translate' in Mdrv[i]:
                mc.setAttr(Mdrv[i], flt[f]*-1)
            else:
                mc.setAttr(Mdrv[i], flt[f])
            if 'translateX' in Mdrn[i] or 'rotateY' in Mdrn[i] or 'rotateZ' in Mdrn[i]:
                mc.setAttr(Mdrn[i], val[f]*-1)
            else:
                mc.setAttr(Mdrn[i], val[f])
            mc.setDrivenKeyframe(Mdrn[i], cd=Mdrv[i])
            for j in range(len(idx)):
                if 'fixed' == d[j]:
                    x = mc.keyTangent(a, q=True, ia=True)
                    y = mc.keyTangent(a, q=True, iw=True)
                    if 'translateX' in Mdrn[i] or 'rotateY' in Mdrn[i] or 'rotateZ' in Mdrn[i]:
                        mc.keyTangent(k, e=True, index=(idx[j], idx[j]), ia=x[j]*-1, iw=y[j])
                    else:
                        mc.keyTangent(k, e=True, index=(idx[j], idx[j]), ia=x[j], iw=y[j])
                else:
                    mc.keyTangent(k, e=True, index=(idx[j], idx[j]), itt=d[j])
                if 'fixed' == e[j]:
                    x = mc.keyTangent(a, q=True, oa=True)
                    y = mc.keyTangent(a, q=True, ow=True)
                    if 'translateX' in Mdrn[i] or 'rotateY' in Mdrn[i] or 'rotateZ' in Mdrn[i]:
                        mc.keyTangent(k, e=True, index=(idx[j], idx[j]), oa=x[j]*-1, ow=y[j])
                    else:
                        mc.keyTangent(k, e=True, index=(idx[j], idx[j]), oa=x[j], ow=y[j])
                else:
                    mc.keyTangent(k, e=True, index=(idx[j], idx[j]), ott=e[j])
            mc.setAttr(Mdrv[i], 0)
            mc.setAttr(Mdrn[i], 0)
        mc.setAttr(Mdrv[i], keep)


    

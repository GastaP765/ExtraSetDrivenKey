import maya.cmds as mc
import UI

def attrGet():
	slc = mc.ls(sl=True)
	atls = mc.listAttr(k=True)
	node = []
	drvr = []
	drvn = []
	for i in atls:
		a = mc.connectionInfo('{0}.{1}'.format(slc[0], i), ied=True)
		if a is True:
			b = mc.connectionInfo('{0}.{1}'.format(slc[0], i), sfd=True)
			c = mc.nodeType(b)
			drvn.append('{0}.{1}'.format(slc[0], i))
			if 'animCurve' in '{}'.format(c):
				d = b.split('.')
				node.append(d[0])
				e = mc.connectionInfo('{}.input'.format(d[0]), ied=True)
				if e is True:
					g = mc.connectionInfo('{}.input'.format(d[0]), sfd=True)
					h = mc.nodeType(g)
					k = g.split('.')
					if 'unitConversion' in '{}'.format(h):
						j = mc.connectionInfo('{}.input'.format(k[0]), sfd=True)
						drvr.append(j)
					else:
						drvr.append(g)
	

	b = UI.DrvClass()
	b.orgAttr(drvr, drvn)
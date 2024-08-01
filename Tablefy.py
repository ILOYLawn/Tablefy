#
# Tablefy by Bryon M.
#

settings_type = {
	'col_wid':int,
	'width':int,
	'row_wid':int,
	'start':int,
	'step':int,
	'header':str,
	'title':str,
	'description':str,
	'justify':str,
	'color':bool,
	'colors':list,
	'limits':list
	}

settings = {
	'col_wid':10,
	'width':10,
	'row_wid':3,
	'start':0,
	'step':1,
	'header':'',
	'title':'Table',
	'description':'',
	'justify':'right',
	'color':True,
	'colors':[50, 255, 50, 255, 50, 50, 50, 50, 255],
	'limits':[0, 1, 2]
	}

def Settings(value, setting = str):
	if setting in settings.keys():
		if type(value) == settings_type.get(setting):
			settings.update({setting:value})
		else:
			raise TypeError('That setting cannot be set to that type')
	else:
		raise ValueError("Setting does not exist and cannot be adjusted")

def Justify(j, cw, t):
	"""
	Justify will automatically format the individual values
	for the table to ensure uniformity.
	"""
	if j == 'left':
		return t.ljust(cw)
	elif j == 'right':
		return t.rjust(cw)
	elif j =='center':
		return t.center(cw)
	else:
		print('Invalid justify setting, defaulting to right justify.')
		return t.rjust(cw)

def DetermineColor(colors, limits, inp):
	parseRGB = {0:'R', 1:'G', 2:'B'}
	y = 0
	if inp < limits[0] or inp > limits[len(limits)-1]:
		return '\x1B[97m'
	else:
		while y < (len(limits)):
			if inp <= limits[y]:
				L0 = limits[y-1]
				L1 = limits[y]
				R0 = colors[(y-1)*3]
				G0 = colors[(y-1)*3+1]
				B0 = colors[(y-1)*3+2]
				R1 = colors[y*3]
				G1 = colors[y*3+1]
				B1 = colors[y*3+2]
				y = len(limits)
			else:
				y += 1
		R = str(round(R0+((inp-L0)*((R1-R0)/(L1-L0))))) + ';'
		G = str(round(G0+((inp-L0)*((G1-G0)/(L1-L0))))) + ';'
		B = str(round(B0+((inp-L0)*((B1-B0)/(L1-L0))))) + 'm'
		return '\x1B[30;48;2;' + R + G + B

def GenerateRows(j, cw, w, rw, l):
	"""
	This will generate the rows to the length specified by 'width' and add
	'\n' to the end of each row to ensure that each row looks good with
	no worry about crashing the program for using a list
	that doesn't divide nicely.
	"""
	p = ""
	if settings['color']:
		for x in range(len(l)):
			if (x%w)==0:
				p += '\n\x1b[30;107m' + str(int(x/w)).center(rw) + '\x1b[0m'
			if type(l[x]) != int and type(l[x]) != float:
				p += '\x1b[97m' + Justify(j, cw, 'NaN') + '\x1b[0m'
			else:
				p += DetermineColor(settings['colors'], settings['limits'], l[x]) + Justify(j, cw, str(l[x])) + '\x1b[0m'
	else:
		for x in range(len(l)):
			if (x%w)==0:
				p += '\n\x1b[30;107m' + str(int(x/w)).center(rw) + '\x1b[0m'
			p += Justify(j, cw, str(l[x]))
	return p
		
def GenerateHeader(j, h, start, step, cw, w, rw):
	if h == "":
		header = "\x1B[30;107m" + Justify('left', rw, ' ')
		for x in range(start, w * step + start, step):
			header += Justify(j, cw, str(x))
		header += "\x1B[0m"
		return header
	else:
		if h.endswith('\n'):
			return h
		else:
			return h + '\n'

def BuildTop(t, d, cw, w, rw):
	"""
	This function builds top part of the table, where the
	table title and description reside.
	"""
	if len(t) > (cw*w+rw):
		raise ValueError("Title is too long")
	t = t.center(cw*w+rw)
	t = '\x1B[1;97m' + t + '\x1b[0;97m\n'
	if len(d) > (cw*w+rw):
		q = d.split(' ')
		a = ''
		d = ''
		for x in range(1, len(q)):
			if len(a + q[x-1]) + 1 > (cw*w+rw):
				a = a.center(cw*w+rw)
				a += '\n'
				d += a
				a = q[x-1]
			else:
				a += " " + q[x-1]
		a += " " + q[x]
		a = a.center(cw*w+rw)
		d += a
	else:
		d = d.center(cw*w+rw)
	return t + d + '\x1B[0m\n'

def Tablefy(l=[]):
	if len(l) != 0:
		finished = BuildTop(settings['title'], settings['description'], settings['col_wid'], settings['width'], settings['row_wid']) + GenerateHeader(settings['justify'], settings['header'], settings['start'], settings['step'], settings['col_wid'], settings['width'], settings['row_wid']) + GenerateRows(settings['justify'], settings['col_wid'], settings['width'], settings['row_wid'], l)
		return finished
	else:
		raise ValueError("There must be list of at least length 1 to tablefy.")

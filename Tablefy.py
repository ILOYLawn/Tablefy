settings = {}

def SetSettings(s=[]):
	if len(s) == 12:
		settings.update({'col_wid':s[0], # How many characters wide a column is, default 10
				   'width':s[1], # How many columns wide a table is, default 10
				   'row_wid':s[2], # How many characters wide the row header is, default 3
				   'start':s[3], # Where the header starts counting, default 0
				   'step':s[4], # How many steps between columns, default 1. Does not affect how the data is read
				   'header':s[5], # The header string, default ''. Don't edit unless you know how you want to format it.
				   'title':s[6], # The title of the table.
				   'description':s[7], # The description of the table. Try to keep it short.
				   'justify':s[8], # Where the text leans, default right.
				   'color':s[9], # A bool to determine whether or not you want to color the table, default True
				   'colors':s[10], # A list of values that must be divisible by 3. [R0, G0, B0, R1, G1, B1]. Default [50, 255, 50, 255, 50, 50]
				   'limits':s[11]}) # List of limits to help determine the colors. L0 is the most RGB0 value, L1 is the most RGB1 value, etc.
	else:
		if len(s) > 12:
			raise ValueError("Length of settings list is too long")
		else:
			raise ValueError("Length of settings list is too short")
	

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
	if inp < limits[0]:
		raise ValueError("Value below lowermost limit!")
	if inp > limits[len(limits)-1]:
		raise ValueError("Value above uppermost limit!")
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
			y = y + 1
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
				q = '\n\x1b[30;107m' + str(int(x/w)).center(rw) + '\x1b[0m'
				p = p + q
			p = p + DetermineColor(settings['colors'], settings['limits'], l[x]) + Justify(j, cw, str(l[x])) + '\x1b[0m'
	else:
		for x in range(len(l)):
			if (x%w)==0:
				q = '\n\x1b[30;107m' + str(int(x/w)).center(rw) + '\x1b[0m'
				p = p + q
			p = p + Justify(j, cw, str(l[x]))
	return p
		
def GenerateHeader(j, h, start, step, cw, w, rw):
	if h == "":
		header = "\x1B[30;107m" + Justify('left', rw, ' ')
		for x in range(start, w * step + start, step):
			header = header + Justify(j, cw, str(x))
		header = header + "\x1B[0m"
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
				a = a + '\n'
				d = d + a
				a = q[x-1]
			else:
				a = a + " " + q[x-1]
		a = a + " " + q[x]
		a = a.center(cw*w+rw)
		d = d + a
	else:
		d = d.center(cw*w+rw)
	return t + d + '\x1B[0m\n'

def Tablefy(l=[], s=[]):
	SetSettings(s)
	if len(l) != 0:
		finished = BuildTop(settings['title'], settings['description'], settings['col_wid'], settings['width'], settings['row_wid']) + GenerateHeader(settings['justify'], settings['header'], settings['start'], settings['step'], settings['col_wid'], settings['width'], settings['row_wid']) + GenerateRows(settings['justify'], settings['col_wid'], settings['width'], settings['row_wid'], l)
		return finished
	else:
		raise ValueError("There must be list of at least length 1 to tablefy.")

import Tablefy as t
"""
To find out more about all settings that can be updated, run:
print(t.settings_type)

'colors' must be a set of ints
'limits' can be ints or floats
"""
inp = []
for x in range(519):
    inp.append(x)
inp.append(519.9)

t.Settings('Pretty Colors', 'title')
t.Settings("Aren't they so pretty?", 'description')
t.Settings(7, 'col_wid')
t.Settings([0,260,520], 'limits')
print(t.Tablefy(inp))
t.Settings([50,100,150], 'limits')
print(t.Tablefy(inp))

inp.clear()
for x in range(22):
    inp.append("Hello!")
t.Settings("Trying To Print Strings As Numbers", 'title')
t.Settings("Why are letters not numbers?", 'description')
t.Settings(True, 'color')
print(t.Tablefy(inp))

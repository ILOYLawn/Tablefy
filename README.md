**NEW**
Added lots of functionality. Now it is recommended to import Tablefy as t, and settings are no longer added as a long variable during the creation of the table. Instead, you can use t.Settings(value, setting) where setting is the setting you wish to edit and value is what you're changing the value to. You can also use t.settings_type and t.settings_type.keys() to 

Tablefy is a table making program design to output a color-coded (ints/floats only) table of inputs, regardless of the size of the list. It is not recommended to use it for lists of strings, but if you do, set 'color' to False using
t.Settings(False, 'color').

You can have a title of length equal to the overall width of the table and a description of any length.
t.Settings('Table', 'title')
t.Settings('What a wonderful table description', 'description')

If you want to use the color function, make a list of ints according to the RGB value of the colors you want using t.Settings([R0, G0, B0, R1, G1, B1,...], 'colors').
[255, 50, 50, 50, 255, 50] is a list of two colors according to Tablefy.
DO NOT make a list of lists. 
After that, set a list of ints or floats to be the limits for the table using
t.Settings([L0, L1,...], 'limits'). 
[0, 100] is a list of limits. These limits will be used to compare the value at a certain position and determine the color. Values outside these limits no longer raise exceptions, but instead are simply not colored. Inputs that are not ints or floats will be changed to NaN and not be colored if 'color' is set to True. If 'color' is set to False, it will attempt to 

Using the above colors and limits, a value of 0 will present as 255, 50, 50 (A nice red) and a value of 100 will present as 50, 255, 50 (a nice green) and any value between will cleanly transition between the two. You can have as many colors and as many limits as you like.

Tablefy returns a value as a single string and can be used to assign tables to variables.

Coming soon:
1. Color-coded strings if I can figure out dictionaries
2. String shortening for strings longer than the col_wid value
3. A better way to get RGB values into the settings

8/1/24

Tablefy is a table making program design to output a color-coded (ints/floats only) table of inputs, regardless
of the size of the list. It is not recommended to use it for lists of strings, but if you do, set 'color' to False.
You can have a table of length equal to the overall width of the table and a description of any length.

If you want to use the color function, make a list of ints according to the RGB value of the colors you want.
DO NOT make a list of lists. After that, set a list of ints for the limits for the table. These limits will be
use to compare the value at a certain position and determine the color. Values outside these limits currently
raise an exception, but I will work on that at some point.

[255, 50, 50, 50, 255, 50] is a list of two colors according to Tablefy.
[0, 100] is a list of limits.
Using these two values, a value of 0 will present as 255, 50, 50 (A nice red) and a value of 100 will present
as 50, 255, 50 (a nice green) and any value between will cleanly transition between the two. You can have as
many colors and as many limits as you like.

Tablefy returns a value as a single string and can be used to assign tables to variables.

Coming soon:
1. Inputs outside of limits allowed
2. Easier time changing settings
3. NaN values
4. Color-coded strings if I can figure out dictionaries

7/6/24

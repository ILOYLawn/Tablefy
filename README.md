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

Below is some code to copy and paste to test and play with the Tablefy program.

from Tablefy import Tablefy

inp = []
for x in range(520):
    inp.append(x)
settings = [10, # This is the column width, or 'col_wid' and determines how many characters wide your columns will be. Default 10
            10, # This is the width and determines how many columns wide your table will be, default 10.
            3,  # This is the row width, or 'row_wid', and determines how many characters wide the row header will be. Default 3.
            0,  # This is the number the header will begin to generate from. Default 0
            1,  # This is the step, or what will be added to the last column to head the current column. Default 1
            '', # This is the header. It is blank by default, but you can input your own string if you don't want an automatically generated one.
            'Title',    # This is the title of the table and will display in bold white text above your table.
            'Description of the table', # This is the description of the table and will display in standard white white text below the title.
            'right', # This is the 'justify' value and will let you decide where in the table your headers and values will sit, default right.
            True, # This is the 'color' setting and will determine whether or not your table will attempt to color the values.
            # Set to False if your values are not ints/floats. 
            [50, 255, 50, 255, 50, 50, 50, 50, 255], # This is the 'colors' list and will be parsed into RGB values to color the table with.
            #R0,  G0, B0,  R1, G1, B1, R2, G2,  B2
            [0, 260, 520]   # This is the limits value which will set at what value you get a certain color.
            #L0, L1,  L2 ... Between L0 and L1, you get a color between RGB0 and RGB1
            ]

print(Tablefy(inp, settings))

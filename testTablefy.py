from Tablefy import Tablefy


inp = []
for x in range(519):
    inp.append(x)
inp.append(519.9)
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
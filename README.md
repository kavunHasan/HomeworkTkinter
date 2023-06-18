# HomeworkTkinter
Created a gui with only given directions by lecturer

# Directions:
Gui:
Prepare an application with graphical user interface.
  Use Tkinter Library
  User should have ZSafe, ZBottom. ZSurface,Feedrateslow, Feedratefast entry boxes.
  User should have a "CONVERT FİLE” Button.
Operation:
  User should enter the ZSafe, ZBottom, Zsurface, Feedrateslow, Feedratefast values in millimeters, and
When click on the "CONVERT” button;
  Should see the source files with ".txt" extension,
  Select the file and convert the data from source file to a destination file in desired format.
Formatting specifications for the destination file:
  If source filename is "filename.txt", then destination filename should be "filename.nc"
  Add following lines to the beginning of the file data
    G90 \n
    M03 sıooo \n
  Add following line to the end of the file (just before closing the file).
    M05 \n
    M02 \n
  Add following lines, for each line starting with ”X” and containing "Y", and ignore the other lines:
    G1 Zsafe Ffeedratefast
    G0 Xxvalue Yyvalue
    G1 Zsurface Ffeedratefast
    G1 Zbottom Ffeedrateslow
Note: X and y values are coordinates in inches/10000 scale and should be converted to milllimeters. 1 inch = 25.4mm

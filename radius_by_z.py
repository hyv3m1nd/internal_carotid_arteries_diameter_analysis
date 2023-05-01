# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 10:41:01 2019
@author: Ben
Files needed: 
    constants.py
    excel.py
    import_modules.py
    an excel file with filename matching the input_name in constants.py
This is the main function.
Input: 
    An excel file containing: 
        A list of points with (x,y,z) coordinates,
        A list of radiuses for each point.
Output:
    A txt file containing: 
        A list of max radiuses for each height level.
    The values in this file can be copied into a new column in the input excel file.
Notes: 
    The excel file must be sorted by z-values, from smallest to largest.
    The input and output file names are defined in constants.py.
"""

#imports 3 files
#import_modules.py, constants.py, and excel.py must be in the same folder
from import_modules import *
from constants import *
import excel

#pd is the pandas python module. It is imported from import_modules. 
#It provides the capacity to read and write excel files
#input_name is imported from constants.py
data = pd.read_excel(input_name);

#Parses the excel file into a list of headers, radiuses, and z-values
#Excel refers to excel.py, which contains my custom functions for parsing excel files
headers = excel.get_headers(data); #this variable is unused
radiuses = excel.get_targets(data);
z_vals = excel.get_sort_values(data);

#Opens a txt file to write the results in
#output_name is imported from constants.py
writer = open(output_name,"w+");

#Walk down our list of points. 
#For each point i, compare its radius to that of every point j with similar z-values.
#Uses max_radius to keep track of the maximum radius of the current z-level.
num_rows = z_vals.size; #this ensures we only walk through rows with defined points
#row_tracker keeps track of which rows' z-values are too small of be relevant.
#It prevents us from having to re-visit every row
row_tracker = 0;
#Walk through every point
for i in range(0,num_rows):
    z_i = z_vals[i]; #current z-value
    max_radius = radiuses[i]; #the radius of our current point is our default max
    #Walk through every point with similar z-values
    for j in range(row_tracker,num_rows):
       z_j = z_vals[j];
       #Two boolean variables that tell us if we are in range
       #relative_min_z and relative_max_z are imported from constants.py
       greater_than_min = z_j > z_i+relative_min_z;
       less_than_max = z_j < z_i+relative_max_z;
       #If the current z-value is too small, update row_tracker.
       #row_tracker is fed into the second for-loop.
       #This ensures we do not re-visit this point on subsequent loops.
       if not greater_than_min:
           row_tracker = j;
       #If the current z-value is too big, stop comparing.
       if not less_than_max:
           break;
       #This boolean variable combines the two in-range booleans
       in_range = z_j > greater_than_min and less_than_max;
       #This point's z-value is close enough to the z-value of our targeted point.
       #Compare the radius.
       #Update max_radius if needed
       if in_range:
           radius_j = radiuses[j];
           new_max_radius = radius_j > max_radius;
           if new_max_radius:
               max_radius = radius_j;
    #We have now compared the radius of our current point 
    #to that of every point with simiar z-values.
    #Print us a status report.
    print("column: ", i+2);
    print("max_radius: ",max_radius);
    #Write the max radius to our output file.
    writer.write(str(max_radius)+"\n");

#We have scanned through our list of points and produced a list of max_radius for each point's z level.
writer.close();
print("finished");




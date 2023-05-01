# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 10:51:20 2019
@author: Ben
"""

from import_modules import *
from constants import *

#From data, extract a list of headers of independent variables. 
#Do this by 
#(1) extracting a list of headers
#(2) removing the header of the independent variable, as defined by target_name
#Note: target_name is defined in constants.py
def get_headers(data):
    headers = data.columns.tolist()
    headers.remove(target_name)
    return headers

#From data, extract a list of radiuses
#Note: target_name is defined in constants.py
def get_targets(data):
    targets = data[target_name];
    return targets;

#From data, extract a list of z-values
#Note: sort_name is defined in constants.py
def get_sort_values(data):
    sort_values = data[sort_name];
    return sort_values;
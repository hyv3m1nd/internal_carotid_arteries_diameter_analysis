# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 10:07:58 2019
@author: Ben

This file imports standard packages for reading pdf 
For this to work properly, you will need to install pandas, sklearn, and graphviz
"""

#Importing required libraries
import os
import os.path
os.environ["PATH"] += os.pathsep + 'C:\Program Files (x86)\Graphviz2.38\bin'
import pandas as pd #reads excel files
import seaborn as sns #gives plots
import matplotlib.pyplot as plt #used by seaborn
from sklearn.ensemble import RandomForestClassifier #one type of classifier 
from sklearn.svm import SVC #another type of classifier (stands for "support vector classifier" in the "support vector model" package)
from sklearn import svm
from sklearn.neural_network import MLPClassifier #classifier 3 (neural network, from multi-layered perceptron classifier)
from sklearn import tree #classifier 3 (decision tree)
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree.export import export_text
#from sklearn.linear_model import SGDClassifier
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.preprocessing import StandardScaler, MinMaxScaler, LabelEncoder
from sklearn.model_selection import train_test_split #split data
import graphviz #visualizes graphs and trees
#%matplotlib inline #this is only required on jupyter notebook
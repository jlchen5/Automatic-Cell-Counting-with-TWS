# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 09:25:36 2021

@author: Theo, Tyler
File architect: creates the single named classifier in output folders for the experimental dataset run
"""

import os

#set the location of the source folder where the folder is installed. 
#CLASS_ORIGIN =  "../tyler_test_area/Classifiers/"
SOURCE = "../training_area/"

#locate classifiers
CLASS_ORIGIN =  SOURCE + "Classifiers/"


#determing the number of classifiers
class_list_pre_trim = os.listdir(CLASS_ORIGIN)
#print(class_list_pre_trim)
type(class_list_pre_trim)


#trim the classifier names of the ".model" at the end
class_list = []
for x in class_list_pre_trim:
    name = x.split('.model')
    class_current = [(name[0])]
    class_list += class_current
print(class_list)
    
#make folders in locations
OUTPUT = SOURCE + "Weka_Output/"
OUTPUT_thresh = SOURCE + "Weka_Output_Thresholded/"
OUTPUT_project = SOURCE + "Weka_Output_Projected/"
OUTPUT_count = SOURCE + "Weka_Output_Counted/"

    

#create classifier folders in each prescribed location
for class_ID in class_list:
    print(class_ID)
    os.mkdir(OUTPUT + class_ID)
    os.mkdir(OUTPUT_thresh + class_ID)
    os.mkdir(OUTPUT_project + class_ID)
    os.mkdir(OUTPUT_count + class_ID)
    

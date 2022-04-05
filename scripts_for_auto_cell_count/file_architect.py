#!/usr/bin/python
###
# Author: Theo Kataras, Tyler Jang
# Date: 4/5/2022
#
# Input: The source directory
#       (optional) The classifier selected by the user for the full dataset
# Output: Directories in training_area or testing_area
# Description: Creates the correct number of classifier folders in output
#              folders.
###
import os
import sys

print("Starting file_architect.py")
# Method to change working directory from inputted ImageJ Macro
curr_dir = os.getcwd()
def set_dir(arg1):
    curr_dir = arg1
    os.chdir(curr_dir)
set_dir(sys.argv[1])

# Boolean to flag if the program is in the testing stage
test_stage = False
if len(sys.argv) == 3:
    class_list_pre_trim = []
    class_list_pre_trim.append(sys.argv[2])

    # Set the location of the source folder where the folder is installed. 
    source = "../testing_area/"
    class_origin =  source + "Classifiers/"
    test_stage = True
else:
    # Set the location of the source folder where the folder is installed. 
    source = "../training_area/"
    # Locate classifiers
    class_origin =  source + "Classifiers/"
    # Determine the number of classifiers
    class_list_pre_trim = os.listdir(class_origin)

# Trim the classifier names of the ".model" at the end
class_list = []
for x in class_list_pre_trim:
    name = x.split('.model')
    class_current = [(name[0])]
    class_list += class_current
print(class_list)
    
# Make folders in locations
output = source + "Weka_Output/"
output_prob = source + "Weka_Probability/"
output_prob2 = source + "Weka_Probability_Projected/"
output_project = source + "Weka_Output_Projected/"
output_count = source + "Weka_Output_Counted/"
results_folder = source + "Results/"
training_folder = source + "training_images/"
valid_folder = source + "Validation_Hand_Counts/"
valid_data_folder = source + "Validation_data/"
class_folder = source + "Classifiers/"

# Create folders in described paths
if not os.path.isdir(output):
    os.mkdir(output)
if not os.path.isdir(output_prob):
    os.mkdir(output_prob)    
if not os.path.isdir(output_prob2):
    os.mkdir(output_prob2)    
if not os.path.isdir(output_project):
    os.mkdir(output_project)
if not os.path.isdir(output_count):
    os.mkdir(output_count)
if not os.path.isdir(results_folder):
    os.mkdir(results_folder)
if not os.path.isdir(training_folder) and not test_stage:
    os.mkdir(training_folder)
if not os.path.isdir(valid_folder) and not test_stage:
    os.mkdir(valid_folder)
if not os.path.isdir(valid_data_folder) and not test_stage:
    os.mkdir(valid_data_folder)
if not os.path.isdir(class_folder) and not test_stage:
    os.mkdir(class_folder)

# Create classifier folders in each prescribed location if it doesn't exist
for class_ID in class_list:
    if not os.path.isdir(output + class_ID):
        os.mkdir(output + class_ID)
    if not os.path.isdir(output_prob + class_ID):
        os.mkdir(output_prob + class_ID)    
    if not os.path.isdir(output_prob2 + class_ID):
        os.mkdir(output_prob2 + class_ID)    
    if not os.path.isdir(output_project + class_ID):
        os.mkdir(output_project + class_ID)
    if not os.path.isdir(output_count + class_ID):
        os.mkdir(output_count + class_ID)

# Generate classifier subfolders for audit directories
if test_stage:
    if not os.path.isdir(source + "Audit_Images/"):
        os.mkdir(source + "Audit_Images/")
    if not os.path.isdir(source + "Audit_Images/" + class_list[0]):
        os.mkdir(source + "Audit_Images/" + class_list[0])

    if not os.path.isdir(source + "Audit_Hand_Counts/"):
        os.mkdir(source + "Audit_Hand_Counts/")
    if not os.path.isdir(source + "Audit_Hand_Counts/" + class_list[0]):
        os.mkdir(source + "Audit_Hand_Counts/" + class_list[0])

    if not os.path.isdir(source + "Audit_Counted/"):
        os.mkdir(source + "Audit_Counted/")
    if not os.path.isdir(source + "Audit_Counted/" + class_list[0]):
        os.mkdir(source + "Audit_Counted/" + class_list[0])
    
    if not os.path.isdir(source + "images/"):
        os.mkdir(source + "Audit_Counted/")
print("Finished file_architect.py")

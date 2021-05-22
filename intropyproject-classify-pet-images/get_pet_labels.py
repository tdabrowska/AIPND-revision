#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: Teresa Dabrowska
# DATE CREATED: 04.01.2021                                 
# REVISED DATE: 
# PURPOSE: Create the function get_pet_labels that creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
from os import listdir

# TODO 2: Define get_pet_labels function below please be certain to replace None
#       in the return statement with results_dic dictionary that you create 
#       with this function
# 
def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels that are returned by the classifier function, since the 
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
      List. The list contains for following item:
         index 0 = pet image label (string)
    """
#     filename_list = listdir('pet_images/')
    filename_list = listdir(image_dir)
    label_list = []
    for i in filename_list:
        if filename_list[0] != ".":
            label_splitted = i.split('_')
            label = ""
            for word in label_splitted:
                if word.isalpha():
                    label += word + " "
            label = label.lower().strip()
            label_list.append(label)
#     print(label_list)
#     print(filename_list)
#     print(len(filename_list))
#     print("\n Prints 10 filenames from folder pet_images/")
#     for idx in range(0, 10, 1):
#           print("{:2d} file: {:25}".format(idx + 1, filename_list[idx]))
          
    
#     Replace None with the results_dic dictionary that you created with this
    # function
    results_dict = {}
    items_in_dict = len(results_dict)
    print('\nEmpty Dictionary results_dict - n items=', items_in_dict)
    
    for idx in range(0, len(filename_list)):
        if filename_list[idx] not in results_dict:
           results_dict[filename_list[idx]] = [label_list[idx]]
        else: 
            print("**Warning: Key=", filename_list[idx],
                  "already exists in results_dict with value=",
                  results_dict[filename_list[idx]])
                    
    print("\n Printing all key-value pairs in dictionary results_dict:")              
    for key in results_dict:
        print("Filename=", key, "   Pet Label=", results_dict[key][0])
                    
    return results_dict

import os
import shutil
import json
import re

with open('config.json') as f:
    dict = json.load(f)
    #print(dict)
input_dnawise = dict['input_dnawise']
input_mednawise = dict['input_mednawise']
input_skin = dict['input_skin']
input_sleep = dict['input_sleep']
destination_dir = dict['destination_dir']
ID_list = []
#print(input_dnawise)
#input 
# input_dnawise ='D:/meemansa2/scripts/sorting_files_ID/dummy_input_folder/DNAwise'
# input_mednawise = 'D:/meemansa2/scripts/sorting_files_ID/dummy_input_folder/MEDNAwise'
# input_skin = 'D:/meemansa2/scripts/sorting_files_ID/dummy_input_folder/SKIN'
# input_sleep = 'D:/meemansa2/scripts/sorting_files_ID/dummy_input_folder/SLEEP'
# destination_dir = 'D:/meemansa2/scripts/sorting_files_ID'
directory_list =[input_dnawise, input_mednawise, input_skin, input_sleep]

# Specify the directory name
#directory_name = "GFG"

def creating_ID_folders():
    input_files = os.listdir(input_dnawise)
    
    for i in input_files:
        filename, ext = os.path.splitext(i) #split the extension from the file name
        split_filename = filename.split('_')
        #print(split_filename[0])
        ID = split_filename[0]
        ID_list.append(ID)
    # Create the directories according to DNAwise IDs - src:GFG
        try:
            os.mkdir(ID)
            print(f"Directory '{ID}' created successfully.")
        except FileExistsError:
            print(f"Directory '{ID}' already exists.")
        except PermissionError:
            print(f"Permission denied: Unable to create '{ID}'.")
        except Exception as e:
            print(f"An error occurred: {e}")

def sorting_files():
    for folder in directory_list:
        files_to_copy = os.listdir(folder) 
        for ID in ID_list:
            for report in files_to_copy:
                if report.startswith(ID):
                    src_path = os.path.join(folder, report)
                    ID_folder = os.path.join(destination_dir, ID)
                    dest_path = os.path.join(ID_folder, report)
                    if os.path.exists(src_path) == True:
                    # and filename.endswith("AKC")
                        try:
                            shutil.copy(src_path, dest_path)
                            # print("File copied successfully.")
                        # If source and destination are same
                        except shutil.SameFileError:
                            print("Source and destination represents the same file.")
                    # If there is any permission issue
                        # except PermissionError:
                        #     print("Permission denied.")
                    # for for not present
                    #     except FileNotFoundError:
                    #         print(f"{ID} not present in {folder}" )
                # For other errors
                        except:
                            print("Error occurred while copying file.")
                    else:
                        print(f"{ID} not present in {folder}" )

def rename_product():
    #for new_folders in os.listdir(destination_dir):
        for ID in ID_list:    
            ID_folder = os.path.join(destination_dir, ID)
            # for testing
            print(f"\nProcessing folder: {ID_folder}")
            for new_files in os.listdir(ID_folder):
                name, ext = os.path.splitext(new_files)
                src_file = os.path.join(ID_folder, new_files)
                if '_' not in name:
                    # rename to what you want to rename it 
                    new_name = ID + '_' + 'Medication'
                    dest_file = os.path.join(ID_folder, new_name + ext)
                    os.rename(src_file, dest_file)
                    #print('MEDNAwise')
                elif 'SKIN' in name:
                    new_name = ID + '_' + 'SKIN'
                    dest_file = os.path.join(ID_folder, new_name + ext)
                    os.rename(src_file, dest_file)
                    #print('DNAwise SKIN')
                elif 'SLEEP' in name:
                    new_name = ID + '_' + 'SLEEP'
                    dest_file = os.path.join(ID_folder, new_name + ext)
                    os.rename(src_file, dest_file)
                    #print('DNAwise SLEEP')
                elif re.search(rf'^{ID}_',name):
                    new_name = ID + '_' + 'Wellness'
                    dest_file = os.path.join(ID_folder, new_name + ext)
                    os.rename(src_file, dest_file)
                    #print('DNAwise')
            
            
    
#creating_ID_folders()
#sorting_files()
#rename_product()
#print(directory_list)

# entering file names according to the matching IDs
# output files forall products start with ID always.

# def sort_files_to_ID_folders():
#     # for DNAwise
#     pass
    


    
    
       

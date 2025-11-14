# Source - https://stackoverflow.com/a
# Posted by sharat87
# Retrieved 2025-11-13, License - CC BY-SA 3.0
'''import os
name, ext = os.path.splitext(fname)
os.rename(fname, name + '2007' + ext)
'''
#print("please input a batch name and number:")
#batch = input() 


import os
from utils import load_config
import argparse

#Paste the path to the directory where the files are in the config.yaml file at 'dir_path'
#load config
config = load_config()

def add_string(config, batch):
    dir_path = config["dir_path"]
    try:
        input_files = os.listdir(dir_path)
    except:
        print(f"File was not found in {dir_path}")
        return
    
    for i in input_files:
        old_path = os.path.join(dir_path, i)
        name, ext = os.path.splitext(i)
        new_name = name + '_' + batch + ext
        new_path = os.path.join(dir_path, new_name)
        os.rename(old_path, new_path)
        #directly renaming the old full path with the new full path, because the script is in a different folder than the fiel 
        pass
    print("Files renamed!")

if __name__=="__main__":
    parser = argparse.ArgumentParser(description='Adds the batch name (Batch-XXX) in front of the file name')
    parser.add_argument("--batch", type=str)
    args = parser.parse_args()
    add_string(config, args.batch)


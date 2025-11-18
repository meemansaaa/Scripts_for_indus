## File Sorting and Renaming Script
This Python script is designed to automate the organization of files into ID-based folders, copy them from multiple input directories, and rename them according to a standardized naming convention. It is especially useful when working with datasets where files are associated with unique IDs across different categories such as DNAwise, Medication, Skin, and Sleep reports

---
### Requirements:
* Python 3.x
* Libraries:
    * os 
    * shutil 
    * json
    * re

### Configuration
The script uses a config.json file to specify input directories and the destination directory.

### Usage
1. Make a folder in the Working Directory  nmed 'input_files' and paste all the files needed to be sorted in that folder
2. Place your files in the appropriate input directories as defined in config.json
3. Run the script
4. Functions in the script:
    * creating_ID_folders() - created folders based on the ID of the files (when in format: ID_XXXXX)
    * sorting_files() - sorting files to their individual folders according to their IDs
    * rename_product() - can rename the files according to their product , keeping their IDs intact in the format 'ID_productname'

Tip: You can comment uncomment the functions according to your requirements.

### Notes
* Only files starting with the ID are moved into the corresponding folder.

* If a folder or file already exists, the script prints a warning but continues processing.

* Files without underscores are assumed to be of a certain type by default.
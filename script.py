import sys
import os
import shutil
import datetime

def main(source_directory, destination_directory, saved_file, date):
    if not os.path.isdir(source_directory):
        raise NotADirectoryError(f"The source directory '{source_directory}' is invalid.")

    directory_files = os.listdir(source_directory)
    
    for file in directory_files:
        try:
            if file == saved_file:
                source_path = f"{source_directory}/{saved_file}"
                shutil.copy({source_path}, destination_directory)
                new_path = f"{destination_directory}/{saved_file} {date}"
                shutil.move(f"{destination_directory}/{file}", new_path)
                # change extension to .tar later
        except:
            print(f"unable to find file" + saved_file)
            sys.exit()
    
    check_saves(destination_directory)


def check_saves(desination_directory):
    directory_files = os.listdir(desination_directory)
    
    # for file in directory_files:
    #     if ''
    
    

if __name__ == "__main__":
    source_directory = sys.argv[1]
    destination_directory = sys.argv[2]
    saved_file = sys.argv[3]
    date = datetime.datetime.now().date()
    main(source_directory, destination_directory, saved_file, date)
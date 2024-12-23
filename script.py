import sys
import os
import shutil
import datetime

def copy_file(source_directory, destination_directory, saved_file, date, days):
    # Check if source directory exists
    if not os.path.isdir(source_directory):
        raise NotADirectoryError(f"The source directory '{source_directory}' is invalid.")
    
    # Check if destination directory exists
    if not os.path.exists(destination_directory):
        os.makedirs(destination_directory)

    source_path = os.path.join(source_directory, saved_file)
    if not os.path.isfile(source_path):
        print(f"File '{saved_file}' not found in source directory.")
        return

    # Change extension to .tar
    tar_file_name = f"{os.path.splitext(saved_file)[0]}_{date}.tar"
    destination_path = os.path.join(destination_directory, tar_file_name)
    
    # Copying the file over to destination directory
    try:
        shutil.copy(source_path, destination_path)
        print(f"File backed up as: {destination_path}")
    except Exception as e:
        print(f"An error occurred during file backup: {e}")

    check_saves(destination_directory, days)


def check_saves(destination_directory, days):
    current_date = datetime.datetime.now().date()
    directory_files = os.listdir(destination_directory)

    # Iterate files in the destination directory
    for file in directory_files:
        try:
            if file.endswith(".tar"):
                # Get the date of the file within the title
                file_date_str = file.split("_")[-1].replace(".tar", "")
                try:
                    file_date = datetime.datetime.strptime(file_date_str, "%Y-%m-%d").date()
                except ValueError:
                    print(f"Skipping file '{file}' with unexpected date format.")
                    continue
                
                age_in_days = (current_date - file_date).days
                # Check if file is older than days specified
                if age_in_days > int(days):
                    file_path = os.path.join(destination_directory, file)
                    os.remove(file_path)
                    print(f"Deleted old file: {file}")
                else:
                    print(f"File is recent: {file} (Age: {age_in_days} days)")
        except Exception as e:
            print(f"Error processing file '{file}': {e}")


if __name__ == "__main__":
    if len(sys.argv) < 5:
        print("Usage: python script.py <source_directory> <destination_directory> <saved_file> <days_before_deletion>")
        sys.exit(1)

    source_directory = sys.argv[1]
    destination_directory = sys.argv[2]
    saved_file = sys.argv[3]
    days = sys.argv[4]
    date = datetime.datetime.now().strftime("%Y-%m-%d")
    
    copy_file(source_directory, destination_directory, saved_file, date, days)
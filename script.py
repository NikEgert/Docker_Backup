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
                # Change extension to .tar
                tar_file_name = f"{saved_file.split('.')[0]}_{date}.tar"
                destination_path = f"{destination_directory}/{tar_file_name}"
                
                # Copy and rename to .tar
                shutil.copy(source_path, destination_path)
                print(f"File backed up as: {destination_path}")
        except FileNotFoundError:
            print(f"Unable to find file: {saved_file}")
        except Exception as e:
            print(f"An error occurred: {e}")
    
    check_saves(destination_directory)


def check_saves(destination_directory):
    current_date = datetime.datetime.now().date()
    directory_files = os.listdir(destination_directory)

    print(f"Checking files in destination directory ({destination_directory}):")
    for file in directory_files:
        try:
            # Extract the date from the file name (assuming format: <name>_YYYY-MM-DD.tar)
            if file.endswith(".tar"):
                file_date_str = file.split("_")[-1].replace(".tar", "")  # Extract the date
                file_date = datetime.datetime.strptime(file_date_str, "%Y-%m-%d").date()
                
                # Calculate the difference in days
                age_in_days = (current_date - file_date).days
                if age_in_days > 4:
                    # Delete file if older than 4 days
                    file_path = f"{destination_directory}/{file}"
                    os.remove(file_path)
                    print(f"Deleted old file: {file}")
                else:
                    print(f"File is recent: {file} (Age: {age_in_days} days)")
        except Exception as e:
            print(f"Error processing file {file}: {e}")


if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python script.py <source_directory> <destination_directory> <saved_file>")
        sys.exit(1)

    source_directory = sys.argv[1]
    destination_directory = sys.argv[2]
    saved_file = sys.argv[3]
    date = datetime.datetime.now().strftime("%Y-%m-%d")  # Format date
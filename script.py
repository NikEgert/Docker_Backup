import sys
import os
import shutil
import datetime
import tarfile

def backup_directory_or_file(source_directory, destination_directory, saved_item, date, days):
    # Check if source directory exists
    if not os.path.isdir(source_directory):
        raise NotADirectoryError(f"The source directory '{source_directory}' is invalid.")
    
    # Check if destination directory exists
    if not os.path.exists(destination_directory):
        os.makedirs(destination_directory)

    source_path = os.path.join(source_directory, saved_item)
    if not os.path.exists(source_path):
        print(f"File or directory '{saved_item}' not found in source directory.")
        return

    # Create a .tar file
    tar_file_name = f"{os.path.splitext(saved_item)[0]}_{date}.tar"
    destination_path = os.path.join(destination_directory, tar_file_name)

    try:
        # Compress the directory or file
        with tarfile.open(destination_path, "w") as tar:
            tar.add(source_path, arcname=os.path.basename(source_path))
        print(f"Backup created: {destination_path}")
    except Exception as e:
        print(f"An error occurred during backup: {e}")

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
                    print(f"Deleted old backup: {file}")
                else:
                    print(f"Backup is recent: {file} (Age: {age_in_days} days)")
        except Exception as e:
            print(f"Error processing backup '{file}': {e}")


if __name__ == "__main__":
    if len(sys.argv) < 5:
        print("Usage: python script.py <source_directory> <destination_directory> <saved_item> <days_before_deletion>")
        sys.exit(1)

    source_directory = sys.argv[1]
    destination_directory = sys.argv[2]
    saved_item = sys.argv[3]
    days = sys.argv[4]
    date = datetime.datetime.now().strftime("%Y-%m-%d")
    
    backup_directory_or_file(source_directory, destination_directory, saved_item, date, days)
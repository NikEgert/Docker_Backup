# File Backup Script

This Python script is designed to back up a specified file from a source directory to a destination directory. It also manages older backups by automatically deleting files that exceed a specified age.

## Features

- **File Backup**: Copies the specified file to a destination directory with a timestamped `.tar` extension.
- **Directory Management**: Creates the destination directory if it doesn't exist.
- **Old File Cleanup**: Automatically removes backup files older than a defined number of days.

## Usage

### Command-line Syntax
```bash
python script.py <source_directory> <destination_directory> <saved_item> <days_before_deletion>
```

### Parameters
- `<source_directory>`: The directory containing the file to be backed up.
- `<destination_directory>`: The directory where the backup will be stored.
- `<saved_file>`: The name of the file/directory to back up (e.g., `myfile.txt`, `mydirectory`).
- `<days_before_deletion>`: The number of days after which backup files are considered old and deleted.

### Example
``` bash
python script.py /path/to/source /path/to/destination myfile.txt 4
```

This command backs up `myfile.txt` from `/path/to/source` to `/path/to/destination` and deletes backups older than 4 days.

## How It Works

1. **File Backup**:
   - Validates the existence of the source directory and file.
   - Creates the destination directory if it doesn’t exist.
   - Copies the file/directory to the destination directory with a new name formatted as `filename_YYYY-MM-DD.tar`.

2. **Old File Cleanup**:
   - Iterates through the `.tar` files in the destination directory.
   - Parses the dates from the file/directory names.
   - Deletes files older than the specified number of days.

## Requirements

- Python 3.x
- Standard Python libraries: `os`, `shutil`, `sys`, `datetime`

## Notes

- Ensure you have the necessary permissions to access the specified directories and files.
- Backup files must follow the `filename_YYYY-MM-DD.tar` naming convention to enable proper cleanup.
import os
import re
import sys

def validate_file_names(file_names):
    """
    Validate a list of file names against a specific pattern.
    
    Args:
    file_names (list): A list of file names to be validated.
    
    Returns:
    dict: A dictionary containing the validation results for each file name.
    int: An exit status indicating whether all files are valid or not
    """
    # Define the regular expression pattern
    pattern = r"^numigien=(.*?)\, style=.*?\.png$"
    
    # Compile the pattern for efficient matching
    regex = re.compile(pattern)
    
    # Initialize an empty dictionary to store validation results
    validation_results = {}
    
    # Initialize exit status as 0 (True)
    exit_status = 0
    
    # Iterate over each file name and validate it
    for index, file_name in enumerate(file_names):
        if not regex.match(file_name):
            validation_results[f"{file_name}"] = f"\033[91mNot valid (does not match pattern)\033[0m"
            exit_status = 1
        else:
            validation_results[f"{file_name}"] = "\033[92mValid\033[0m"
    
    # Return the dictionary containing validation results and exit status
    return validation_results, exit_status

# Get a list of files from the 'src' directory
def get_files_from_dir(directory_path):
    """
    Returns a list of file names from the specified directory.
    
    Args:
    directory_path (str): The path to the directory containing files.
    
    Returns:
    list: A list of file names in the specified directory.
    """
    # Initialize an empty list to store file names
    file_names = []
    
    try:
        # Iterate over each item in the directory and append its name to the list
        for filename in os.listdir(directory_path):
            if os.path.isfile(os.path.join(directory_path, filename)):
                file_names.append(filename)
    except FileNotFoundError:
        print("Directory not found. Please ensure the path is correct.")
        return []
    
    # Return the list of file names
    return file_names

# Usage example
directory_path = "src"
file_names = get_files_from_dir(directory_path)
validation_results, exit_status = validate_file_names(file_names)
print("\nValidation Results:")
for key, value in validation_results.items():
    print(f"{key}: {value}")
if exit_status == 1:
    sys.exit(1)
else:
    done_list = []
    valid_count = 0
    invalid_count = 0
    for key, value in validation_results.items():
        if "Valid" in value:
            valid_count += 1
        else:
            invalid_count += 1
            done_list.append(key)
    print("\nSummary:")
    print(f"Done: {len(done_list)}")
    print(f"Valid: {valid_count}")
    print(f"Invalid: {invalid_count}")
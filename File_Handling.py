import os

def list_directory_contents(path):
    try:
        if os.path.exists(path):
            print(f"Contents of directory ({path}):")
            for item in os.listdir(path):
                print(item)
        else:
            print("Invalid directory path.")
    except FileNotFoundError:
        print("The directory does not exist. Please enter a valid path.")
    except PermissionError:
        print("You do not have permission to access this directory.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

directory_path = input("Enter the directory path: ")
list_directory_contents(directory_path)

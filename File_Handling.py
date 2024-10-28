import os

def list_directory_contents(path):
    try:
        if os.path.exists(path):
            print(f"Contents of directory ({path}):")
            for item in os.listdir(path):
                print(item)
        else:
            print("Invalid directory path.")
    except Exception:
        print("Invalid directory or there has been an error.")

directory_path = input("Enter the directory path: ")
list_directory_contents(directory_path)

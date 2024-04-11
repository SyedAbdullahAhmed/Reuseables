import os 

def create_files():
    """
    Creates a specified number of files with a given name and extension in the current working directory.
    """
    choice = 1  # Not used in this implementation, but can be utilized for future enhancements
    no_of_files = int(input("Enter number of files you want to create: "))

    # Get the current working directory
    path = os.getcwd()

    # Get the file name and extension from user input
    file_name = input("Enter file name: ")
    extension_name = input("Enter extension name (e.g., .exe): ")

    # Check if the extension name starts with a dot
    if not extension_name.startswith('.'):
        print("Invalid extension name")
        exit()

    i = 1
    # Create the specified number of files
    while i <= no_of_files:
        # Open and close the file to create it
        with open(os.path.join(path, f"{file_name}{i}{extension_name}"), 'w') as fp:
            pass
        i += 1

    # List the created files
    files = []
    dir_list = os.listdir()
    for item in dir_list:
        if item.startswith(file_name):
            files.append(item)

    # Print the list of created files
    print("Created files:")
    print(files)

# Call the function to execute file creation
create_files()

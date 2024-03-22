import os

# Get the list of files in the current directory

files = os.listdir('.')

print("File: ")
for file in files:
    print(file)

# Create folder
    
# os.mkdir('new_folder')

print(os.name)
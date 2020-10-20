""""
Write a Program that creates files and auto renames my files

to whatever I want and iterates through the files it reaches the end.
"""
import os

# Single Line Space
def space():

    print("\n")
space()

# Function used to get the path of the directory from the user.
def gather_path():
    # Given the Path by the user
    path = input("Please enter the path to your desired Directory: ")

    # Assigns the path to current working directory
    os.chdir(path)

# Runs gather_path function.
gather_path()
space()
# Ensure this is the right location
print("Is this the right Location?: " + os.getcwd() + "\n")

# Answer enter key is pressed.
Answer = str(input("(If Yes, Press enter.)"))

# Number of files in the directory.
file_nm = len(os.listdir())

# List of files in the directory.
file_list = os.listdir()


print("Here are the Files within your directory: ")
space()
print("Disclaimer! Please take a look at the list of files below. ↓")
print("The results WILL be affected if the files are not in the desired order.")
space()
# For loop to display a list of  the files in the directory. f is the file
for f in file_list:
    f_split = (os.path.splitext(f))
    print(f_split)
    # for p, file in enumerate(file_list, start=0):
space()

# Splits File names, f_name is the full file name, and f_ext is the file extension. (file type)
f_name, f_ext = (os.path.splitext(f))

# Input of the new name for the files
print("Format example: Futurama-S01")
new_names = input("Please enter The title format for your files:  ")
space()

# media_name is the name of the Show/Movie, s_e_num is the Season and Episode number.
# The Split uses a hyphen(-) to split the value in to the two variables.
media_name, s_e_num = new_names.split("-")

# Variables Used in the renaming loop.
i = 1
zero = "0"
# While Loop used to get the episode numbers.
while i < file_nm + 1:
    for d in file_list:
        # final_s_e is the variable for the Seasons and Episodes number the final one.
        # Zfill is used to ad the extra zero in front of the numbers less than ten.
        final_s_e = s_e_num + "E" +str(i).zfill(2)
        final_s_e = final_s_e[0:]
        i += 1
        int(i)
        new_name = ("{} {}{}".format(media_name, final_s_e, f_ext))
        os.rename(d, new_name)
        print(d," --> " , new_name)

space()
print("Program is complete! Results are shown above. ↑ ↑ ↑ ")

import sys
#from pathlib import Path
from datetime import datetime
from datetime import date
import shutil
import os 
today = date.today()

date = today.strftime("%b-%d-%Y")

time = datetime.now()
dt_string = time.strftime ("%b-%d-%Y" + " " +"%H-%M-%S")

#print(date)
#print(dt_string)
#print("Session "+ dt_string + ".txt")

home_dir = r"C:Users\shann\Desktop"
source_dir = r"C:\Users\shann\Desktop\Software\Programming\Python\Scripts\Renamer-beta"

sys.stdout = open("Session "+ dt_string + ".txt", "w")

print("Hello World")
print(dt_string)
sys.stdout.close()

f_name = "Session "+ dt_string + ".txt"




#os.rename(source_dir + f_name, home_dir + f_name)

#shutil.move(source, destination)
shutil.move(source_dir + f_name, home_dir + f_name)
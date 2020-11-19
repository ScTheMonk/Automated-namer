import sys
from pathlib import Path
from datetime import datetime
from datetime import date

today = date.today()

date = today.strftime("%b-%d-%Y")

time = datetime.now()
dt_string = time.strftime ("%b-%d-%Y" + " " +"%H-%M-%S")

#print(date)
#print(dt_string)
#print("Session "+ dt_string + ".txt")


sys.stdout = open("Session "+ dt_string + ".txt", "w")

print("Hello World")

sys.stdout.close()

f_name = "Session "+ dt_string + ".txt"

Path(r"C:\Users\shann\Desktop\Software\Programming\Python\Scripts\Renamer-beta"+ f_name + ".text").rename(r"C:\Users\shann\Desktop" + f_name+ ".text")
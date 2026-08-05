from datetime import datetime
import os

from narwhals import Time

current_time = datetime.now()
date = current_time.strftime("%d %B, %Y")
time = current_time.strftime("%I:%M %p")
report_folder = "Reports"
    
os.makedirs(report_folder, exist_ok = True)
folder = os.listdir(report_folder)

file_name = f"{current_time.strftime("Phishing_Analysis_Report_%y_%m_%d")}_{len(folder) + 1 :3}"
file_path = os.path.join(report_folder, file_name)
print(file_name)

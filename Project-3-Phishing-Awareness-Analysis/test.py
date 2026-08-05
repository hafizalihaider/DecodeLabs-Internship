from datetime import datetime

from narwhals import Time

current_time = datetime.now()
date = current_time.strftime("%d %B, %Y")
time = current_time.strftime("%I:%M %p")
print("-"*100)
print(f"{'Date: ' + date:<40}{'Time: ' + time:>30}\n")
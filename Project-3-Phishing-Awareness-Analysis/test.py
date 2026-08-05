from datetime import datetime

current_time = datetime.now()

print(current_time.strftime("%d %B, %Y"))

print(current_time.strftime("%I:%M %p"))
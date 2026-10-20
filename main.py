from datetime import datetime, timedelta
start_time = datetime.now()
now_time = datetime.now()
while (now_time < start_time + timedelta(minutes=10)): # this makes sure our program stops after 10 mins
    print("Hello World")
    # put our code here
    now_time = datetime.now()

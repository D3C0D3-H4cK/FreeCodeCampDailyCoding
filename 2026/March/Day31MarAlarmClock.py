"""
Wake-Up Alarm

Given a string representing the time you set your alarm and a string representing the time you actually woke up, determine if you woke up early, on time, or late.

    Both times will be given in "HH:MM" 24-hour format.

Return:

    "early" if you woke up before your alarm time.
    "on time" if you woke up at your alarm time, or within the 10 minute snooze window after the alarm time.
    "late" if you woke up more than 10 minutes after your alarm time.

Both times are on the same day.
"""
from datetime import datetime, timedelta

def alarm_check(alarm_time, wake_time):
    Alarm = datetime.strptime(alarm_time, "%H:%M")
    Wakeup = datetime.strptime(wake_time, "%H:%M")
    diferencia = Wakeup - Alarm
    if Alarm > Wakeup:
        print("early")
    elif diferencia >= timedelta(minutes=10):
        print("late")
        print(diferencia)
    else:
        print("on time")
    
alarm_check("08:15", "08:25")
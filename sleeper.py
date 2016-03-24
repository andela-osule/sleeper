from datetime import timedelta, datetime


wake_up = raw_input("When do you want to wake up? (12:00AM/PM) ")
hours_to_sleep = int(raw_input("How many hours do you plan on sleeping for? "))

current_time = datetime.today()
wakeup_time = datetime.strptime(wake_up, "%I:%M%p")

delta = timedelta(hours=hours_to_sleep)

wake_up_day = current_time  # find the day user wakes up

wakeup_time = datetime(
    wake_up_day.year, wake_up_day.month, wake_up_day.day,
    wakeup_time.hour, wakeup_time.minute)

adjusted = wakeup_time - current_time - delta

print "Current time is: {}".format(current_time.strftime("%I:%M%p"))

print "Wake up: {}".format(wake_up)

print "Go to sleep in {} hour(s), {} minute(s)".format(
    adjusted.hours, adjusted.minutes)

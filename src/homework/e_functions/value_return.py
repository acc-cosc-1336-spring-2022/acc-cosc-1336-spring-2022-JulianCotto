def get_time(hour, minutes, seconds, time_type, meridiem='AM'):
    if hour < 10:
        hour = "0" + str(hour)

    if minutes < 10:
        minutes  = "0" + str(minutes)

    if seconds < 10:
        seconds = "0" + str(seconds)

    time = str(hour) + ":" + str(minutes) + ":" + str(seconds)

    if time_type == 12:
        time = time + " " + meridiem

    return  time

def get_hour(epoch_seconds):
    return epoch_seconds // 3600

def get_minutes(epoch_seconds):
    return (epoch_seconds // 60) % 60

def get_seconds(epoch_seconds):
    return epoch_seconds % 60

def time_from_utc(utc_offset, utc_zero):
    sum = utc_offset + utc_zero
    return sum % 24

def hour():
    hour = int(input("Please input the current hour"))
    return hour 

def minute():
    minute = int(input("Please input the current minutes"))
    return minute

def second():
    seconds = int(input("Please input the current seconds"))
    return seconds

def time_type():
    time_type = int(input("Please input the current time type - 12/24?"))
    return time_type








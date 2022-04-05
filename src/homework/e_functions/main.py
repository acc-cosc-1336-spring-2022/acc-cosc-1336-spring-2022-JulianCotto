from clock_app import ClockApp

from value_return import get_time, hour, minute, second, time_type

time = get_time(hour(), minute(), second(), time_type())
print(time)


import datetime

def getnowFunc():
    currtime = datetime.datetime.now()
    year = currtime.year
    month = currtime.month
    day = currtime.day
    hour = currtime.hour
    minute = currtime.minute
    second = currtime.second
    result = str(year)+str(month)+str(day)+str(hour)+str(minute)+str(second)
    return result
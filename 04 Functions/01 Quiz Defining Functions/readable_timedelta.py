# write your function here
def readable_timedelta(days):
    week = days // 7
    day = days % 7
    message = "{} week(s) and {} day(s).".format(week, day)
    return message

# test your function
print(readable_timedelta(10))

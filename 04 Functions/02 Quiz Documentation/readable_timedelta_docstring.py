def readable_timedelta(days):
    """
    Convert any number of days into a string in week(s) and day(s) format.
    
    Args:
        days: int. Any number of days.

    Returns:
        readable_timedelta: A string that says how many weeks and days that is. 
    """

    weeks = days // 7
    remainder = days % 7
    return "{} week(s) and {} day(s)".format(weeks, remainder)

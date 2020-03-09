import datetime


def get_today():
    """..............................................................."""
    return datetime.datetime.now()


def get_today_string():
    return get_today().strftime("%Y%M%d")

from dateutil import tz


def convert_utc_to_local(date, timezone=tz.gettz("Europe/Prague")):
    return date.astimezone(timezone)

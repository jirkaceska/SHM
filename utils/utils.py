from dateutil import tz


def convert_utc_to_local(date, timezone=tz.gettz("Europe/Prague")):
    return date.astimezone(timezone)


def get_time_span(start, end):
    if start['start__time__min'] is None or end['end__time__max'] is None:
        return None

    start = convert_utc_to_local(start['start__time__min'])
    end = convert_utc_to_local(end['end__time__max'])

    return {
        'start': start.hour,
        'end': end.hour + 1,
        'range': ["{:02}:00".format(i) for i in range(start.hour, end.hour + 2)]
    }

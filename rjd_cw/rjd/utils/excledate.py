import datetime
def xldate_as_datetime(xldate, datemode=0):
    if datemode not in (0, 1):
        raise Exception(datemode)
    if xldate == 0.00:
        return datetime.time(0, 0, 0)
    if xldate < 0.00:
        raise Exception(xldate)
    xldays = int(xldate)
    frac = xldate - xldays
    seconds = int(round(frac * 86400.0))
    assert 0 <= seconds <= 86400
    if seconds == 86400:
        seconds = 0
        xldays += 1
    # if xldays >= _XLDAYS_TOO_LARGE[datemode]:
    #    raise XLDateTooLarge(xldate)
    if xldays == 0:
        # second = seconds % 60; minutes = seconds // 60
        minutes, second = divmod(seconds, 60)
        # minute = minutes % 60; hour    = minutes // 60
        hour, minute = divmod(minutes, 60)
        return datetime.time(hour, minute, second)
    if xldays < 61 and datemode == 0:
        raise Exception(xldate)
    return (
            datetime.date.fromordinal(xldays + 693594 + 1462 * datemode)
            + datetime.timedelta(seconds=seconds)
    )
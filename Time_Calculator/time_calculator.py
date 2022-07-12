print('Scientific Computing with Python - FreeCodeCamp')
print('Project : Time Calculator')

def add_time(start, duration, weekday=''):

    # This function adds the duration time to the start time, returns the result with the weekday if given, and the amount of days that have passed.

    # start hour arrangement.
    start_hour = int(start[:start.index(':')])
    start_minute = int(start[start.index(':') + 1:-3])

    # duration hour arrangement.
    duration_hour = int(duration[:duration.index(':')])
    duration_minute = int(duration[-2:])

    # total hour and minutes result.
    total_hour = start_hour + duration_hour
    total_minute = start_minute + duration_minute

    # Adequate format for hours and minutes.
    new_hour = total_hour % 12
    if new_hour == 0:
        new_hour = 12

    if total_minute >= 60:
        total_minute -= 60
        new_hour += 1
        total_hour += 1
    new_minute = total_minute

    # Meridian arrangement.
    current_meridian = start[-2:]
    new_meridian = ''
    leap_am_pm = int(total_hour / 12)

    if leap_am_pm % 2 == 0:
        new_meridian = current_meridian
    else:
        new_meridian = [n for n in ('AM', 'PM') if n != current_meridian][0]

    # Days passed.
    days_passed = 0
    if current_meridian == 'PM':
        days_passed = int((leap_am_pm + 1) / 2)
    else:
        days_passed = int((leap_am_pm / 2))

    # Day of the week arrangement

    if weekday:
        week_days = ['Monday', 'Tuesday', 'Wednesday',
                     'Thursday', 'Friday', 'Saturday', 'Sunday']

        current_day = weekday.capitalize()
        position = week_days.index(current_day) + days_passed % 7

        if position < 7:
            new_week_day = week_days[position]
        else:
            new_week_day = week_days[position - 7]

        if days_passed == 0:
            new_hour = f'{new_hour}:{new_minute:02} {new_meridian}, {new_week_day}'
        elif days_passed == 1:
            new_hour = f'{new_hour}:{new_minute:02} {new_meridian}, {new_week_day} ' \
                       f'(next day)'
        else:
            new_hour = f'{new_hour}:{new_minute:02} {new_meridian}, {new_week_day} ' \
                       f'({days_passed} days later)'
    else:
        if days_passed == 0:
            new_hour = f'{new_hour}:{new_minute:02} {new_meridian}'
        elif days_passed == 1:
            new_hour = f'{new_hour}:{new_minute:02} {new_meridian} (next day)'
        else:
            new_hour = f'{new_hour}:{new_minute:02} {new_meridian} ' \
                       f'({days_passed} days later)'

    return new_hour

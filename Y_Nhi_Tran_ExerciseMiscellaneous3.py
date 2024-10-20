# Y Nhi Tran
# Exercise Miscellaneous 3 - TimeDate

from datetime import datetime


def calculate_years_from_now(timedate):
    now = datetime.now()
    time_difference = now - timedate
    years = time_difference.days / 365.25  # accounting for leap years

    return int(years)


# Assuming timedate is a datetime object representing September 11, 2020, at 02:38 PM
timedate = datetime(2020, 9, 11, 14, 38)

years_from_now = calculate_years_from_now(timedate)
print(years_from_now)

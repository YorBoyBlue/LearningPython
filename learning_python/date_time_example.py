import datetime
import pytz

# Naive datetime does not have enough information to handle things like
# daylight savings and timezone but are easiest to work with

# Aware datetime does have enough information to handle things like
# daylight savings and timezone but are harder to work with

# Naive date time examples ====================================================

# Date Example-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

print('\nDATE', '-' * 100)

# Create a basic specific date object
# Year, Month, Day
d = datetime.date(2016, 7, 24)

# Create date object that is today's date
tday = datetime.date.today()
# You can access specific elements of the date object
print()
print("What is today's date?")
print(tday)
print(tday.year)
print(tday.month)
print(tday.day)

print()
print('What is the day of the week?')
# You can access what day od the week it is with these two functions
# Monday = 0 - Sunday = 6
print(tday.weekday())
# Monday = 1 - Sunday = 7
print(tday.isoweekday())

# Time Example-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

print('\nTIME', '-' * 100)

# Create a basic specific time object
# Hour, Minute, Seconds, Microseconds
t = datetime.time(9, 30, 45, 100000)

# Create time object that is now
now = datetime.datetime.now()
time_now = datetime.time(now.hour, now.minute, now.second, now.microsecond)
# You can access specific elements of the time object
print()
print("What is the current time of day?")
print(time_now)
print(time_now.hour)
print(time_now.minute)
print(time_now.second)
print(time_now.microsecond)

# DateTime Example-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

print('\nDATETIME', '-' * 100)

# Create a basic specific datetime object
# Year, Month, Day, Hour, Minute, Seconds, Microseconds
my_date_time = datetime.datetime(2016, 7, 26, 12, 30, 45, 100000)

# Create datetime object that is now
now = datetime.datetime.now()
print()
print("What is the current date and time of day?")
print(now)
print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)
print(now.microsecond)

print()
print("What is the current date from the datetime object?")
print(now.date())

print()
print("What is the current time of day from the datetime object?")
print(now.time())

# Time Deltas-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

print('\nTIME DELTAS', '-' * 100)

# Create a basic time delta object
tdelta = datetime.timedelta(days=7)
# Manipulate a date with a time delta to get a date as a result
print()
print('What is the date one week from today?')
print(tday + tdelta)
print('What was the date one week ago from today?')
print(tday - tdelta)

my_next_bday = datetime.date(2019, 4, 28)
until_bday = my_next_bday - tday
# Manipulate a date with another date to get a time delta as a result
print()
print('Normal Output')
print(until_bday)
print('How many days (time delta) until my next bday?')
print(until_bday.days)
print('How many seconds (time delta) until my next bday?')
print(until_bday.total_seconds())

# You can create time deltas for any element(s) listed below
tdelta = datetime.timedelta(days=7, hours=1, minutes=1, seconds=1,
                            microseconds=100000)
print()
print('What is the current datetime?')
print(now)
print(
    'What is the datetime after our time delta is applied? (TimeDelta = days=7'
    ', hours=1, minutes=1, seconds=1, microseconds=100000)')
print(now + tdelta)

# Aware date time examples ====================================================

# NOT AWARE FIRST THEN MANIPULATE TO AWARE----------

print('\nTIME ZONE AWARE DATETIME', '-' * 100)

# Returns the current local datetime with a time zone of NONE
dt_today = datetime.datetime.today()
# Returns the current local datetime with an option to pass in a time zone
# If a time zone is not passed in it will be the same as the above example
dt_now = datetime.datetime.now()
# Returns the current UTC datetime with a time zone of NONE
dt_utcnow = datetime.datetime.utcnow()
print()
print('today(): ', dt_today)
print('now(): ', dt_now)
print('utcnow(): ', dt_utcnow)

# MANIPULATE TO AWARE----------

# It is recommended to always work with UTC when working with timezones
# Get a specific aware time
# Aware Date Time Result = 2018-06-26 17:12:50.240649+00:00
# +00:00 is the UTC offset (How many hours and minutes are different from UTC)
aware_dtime = datetime.datetime(2016, 7, 26, 12, 30, 45, tzinfo=pytz.UTC)
# This is the recommended approach for current UTC time zone aware datetime
aware_dtime_now_utc = datetime.datetime.now(tz=pytz.UTC)
# This is not the recommended approach for current UTC time zone aware datetime
aware_dtime_utcnow = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)

print()
print('What is the current UTC time zone aware date time?')
print(aware_dtime_now_utc)
print('What is the current (Canada/Mountain) time zone aware date time?')
aware_dtime_now_mtn = aware_dtime_now_utc.astimezone(
    pytz.timezone('Canada/Mountain'))
print(aware_dtime_now_mtn)

# Create a time zone aware datetime from a NAIVE datetime
# Create naive datetime object that is now
now = datetime.datetime.now()
# Create a timezone object for Eastern Time
mtn_tz = pytz.timezone('Canada/Eastern')
print()
print('What is the current local NAIVE datetime?')
print(now)
print(
    'What is the current (Canada/Eastern) time zone aware date time from a '
    'naive datetime object?')
now = mtn_tz.localize(now)
print(now)

# Other date time examples ====================================================

print('\nFORMATS', '-' * 100)
# https://docs.python.org/2/library/datetime.html#strftime-and-strptime-behavior

# Output datetime objects in different formats
now = datetime.datetime.now()
print()
print('This is an international standard')
print(now.isoformat())
print(
    'https://docs.python.org/2/library/datetime.html#strftime-and-strptime-'
    'behavior')
print('This is a custom format to convert datetime object to a string. '
      'See link above for more info.')
print(now.strftime('%B %d, %Y'))

# Convert a string to a datetime object
dt_string = 'June 26, 2018'
dtime = datetime.datetime.strptime(dt_string, '%B %d, %Y')
print('Convert string back to datetime object')
print(dtime)

print()
print('Using format() With Date Objects:')
my_date = datetime.datetime(2018, 9, 24, 12, 30, 45)
sentence = '{}'.format(my_date)
print(sentence)
sentence = '{:%B %d, %Y}'.format(my_date)
print(sentence)

# You can print all the possible time zones that can be passed in in two ways
# I prefer this way
# for tz in pytz.all_timezones:
#     print(tz)
# print(pytz.all_timezones)

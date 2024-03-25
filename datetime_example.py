"""
Get the current date and time.
Add or subtract days from the current date.
Calculate the difference between two dates.
Format dates into more readable strings.
Parse a string to a datetime object.
"""

import datetime

# Get current date and time
now = datetime.datetime.now()
print(f"Current date and time: {now}")

# Add days to the current date
five_days_later = now + datetime.timedelta(days=5)
print(f"Five days from now: {five_days_later}")

# Subtract days from current date
five_days_earlier = now - datetime.timedelta(days=5)
print(f"Five days ago: {five_days_earlier}")

# Calculate the difference between two dates
some_day = datetime.datetime(2023, 1, 1)
difference = now - some_day
print(f"Years since January 1, 2023: {difference.days / 365:.2f} years")
print(f"Days since January 1, 2023: {difference.days} days")

# Format dates into more readable strings
formatted_date = now.strftime("%A, %B %d, %Y %H:%M:%S")
print(f"Formatted curren date and time: {formatted_date}")

# Parse string to a datetime object
date_string = "2024-03-21 12:00:00"
parsed_date = datetime.datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
print(f"Parsed datetime object: {parsed_date}")
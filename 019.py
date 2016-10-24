"""
You are given the following information, but you may prefer to do some research for yourself.

[1] 1 Jan 1900 was a Monday.
[2] Thirty days has September,
    April, June and November.
    All the rest have thirty-one,
    Saving February alone,
    Which has twenty-eight, rain or shine.
    And on leap years, twenty-nine.
[3] A leap year occurs on any year evenly divisible by 4, but not on a century unless it
    is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""

from datetime import datetime
from datetime import timedelta

def main():
  # Note that range -> [start, end).
  start = datetime(1901, 1, 1)
  end = datetime(2001, 1, 1)
  
  # Find first sunday
  date = start + timedelta(days = 6 - start.weekday())
  
  # Count all sundays on the first of the month up to the end date (not inclusive).
  sundays_on_first = 0
  week = timedelta(weeks=1)
  while date < end:
    if date.day == 1:
      sundays_on_first += 1
    date += week
  
  print(sundays_on_first)

if __name__ == '__main__':
  main()

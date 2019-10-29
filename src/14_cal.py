"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py month [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.
"""

import sys
import calendar
from datetime import datetime

date_input = input("14_cal.py month [year]: ")

now = datetime.today(); year = now.year; month = now.month

def error(str):
    print(str)

def strip_date_list_separate(date):
    date = date.replace(',', ' ')
    date = date.replace('/', ' ')
    date = date.replace('  ', ' ')
    date_list = date.split(" ")
    return date_list
    
def print_cal(month, year):
    if int(month) > 12 or int(month) < 1:
        error('invalid month, must be between 1 and 12')
    else:
        cal = calendar.TextCalendar(calendar.SUNDAY)
        cal_str = cal.formatmonth(int(year), int(month))
        print(cal_str)

if not date_input.strip():
    print_cal(month, year)
else:
    date_input = date_input.strip()
    if len(date_input) > 3:
        date_list = strip_date_list_separate(date_input)
        if len(date_list) > 3:
            error("input must be in format: MM YYYY")
        else:
            print_cal(date_list[0], date_list[1])
    else:
        date_list = strip_date_list_separate(date_input)
        print_cal(date_list[0], year)
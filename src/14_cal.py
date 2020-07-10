"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py [month] [year]`
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

Note: the user should provide argument input (in the initial call to run the file) and not
prompted input. Also, the brackets around year are to denote that the argument is
optional, as this is a common convention in documentation.

This would mean that from the command line you would call `python3 14_cal.py 4 2015` to
print out a calendar for April in 2015, but if you omit either the year or both values,
it should use today’s date to get the month and year.
"""

import sys
import calendar

from datetime import datetime

userInput = sys.argv
currentYear = datetime.today().year
currentMonth = datetime.today().month


def isValid(*userInput):
    for el in userInput:
        if (el.isdigit() is False):
            return False
    if (int(userInput[0]) > 12 or int(userInput[0]) < 1):
        return False
    return True


def getCalendar(month, year):
    return calendar.month(year, month, l=2, w=3)


if (len(userInput) is 1):
    print(f"\n{getCalendar( currentMonth,currentYear,)}\n")
elif(len(userInput) is 2):
    if (isValid(userInput[1])):
        print(f"\n{getCalendar( int(userInput[1]),currentYear,)}\n")
    else:
        print("\n[1 >= month <= 12] must be a digit.\n")
elif(len(userInput) is 3):
    if (isValid(userInput[1], userInput[2])):
        print(f"\n{getCalendar( int(userInput[1]), int(userInput[2]))}\n")
    else:
        print("\n[1 >= month <= 12] and [year] must be digits.\n")
else:
    print("\nPlease follow this format: `14_cal.py [month] [year]`\n")

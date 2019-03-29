# Define a daysBetweenDates procedure that would produce the
# correct output if there was a correct nextDay procedure.
#
# Note that this will NOT produce correct outputs yet, since
# our nextDay procedure assumes all months have 30 days
# (hence a year is 360 days, instead of 365).
# 

def isLeapYear(year):
# da Wikipedia
# if (year is not divisible by 4) then (it is a common year)
# else if (year is not divisible by 100) then (it is a leap year)
# else if (year is not divisible by 400) then (it is a common year)
# else (it is a leap year)
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False

def daysInMonth(year, month):
    if month == 1 or month2 == 3 or month == 5 or month == 7 \
        or month == 8 or month == 10 or month == 12:
        return 31
    else:
        if month == 2:
            if isLeapYear(year):
                return 29
            return 28
    return 30

def nextDay(year, month, day):
    """Simple version: assume every month has 30 days"""
    if day < 30:
        return year, month, day + 1
    else:
        if month == 12:
            return year + 1, 1, 1
        else:
            return year, month + 1, 1
        
def dateIsBefore(year1, month1, day1, year2, month2, day2):
    if year1 < year2:
        return True
    if year1 == year 2:
        if month1 < month2
            return True
        if month1 == month2
            return day1 < day2
    return False
        
# def daysBetweenDates(year1, month1, day1, year2, month2, day2):
#   """Returns the number of days between year1/month1/day1
#       and year2/month2/day2. Assumes inputs are valid dates
#       in Gregorian calendar, and the first date is not after
#       the second."""
#       
#    daysInYear = 365
#    totalDays1 = (year1 * daysInYear) + (month1 * daysInMonth) + day1
#    totalDays2 = (year2 * daysInYear) + (month2 * daysInMonth) + day2
#    daysBetweenDates = totalDays2 - totalDays1
#    
#    return daysBetweenDates

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    days = 0  
    year1, month1, day1 = nextDay(year1, month1, day1)
    days += 1
    return days

def test():
    test_cases = [((2012,9,30,2012,10,30),30), 
                  ((2012,1,1,2013,1,1),366),
                  ((2012,9,1,2012,9,4),3)]
    
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print "Test with data:", args, "failed"
        else:
            print "Test case passed!"

test()

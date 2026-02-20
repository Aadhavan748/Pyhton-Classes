# Activity 1 - Current Date and Time

"""from datetime import date, time, datetime

today = date.today()
now = datetime.now()

print("Today's date is", today)
print("Current date and time is", now)

print("Date components", today.year, today.month, today.day)"""

# Activity 2 - Random date and time

import random
import time

def getRandomDate(startDate, endDate ):
    print("Printing random date between", startDate, "and", endDate)
    randomGenerator = random.random()
    dateFormat = '%d/%m/%Y'

    startTime = time.mktime(time.strptime(startDate, dateFormat))
    endTime = time.mktime(time.strptime(endDate, dateFormat))

    randomTime = startTime + randomGenerator * (endTime - startTime)
    randomDate = time.strftime(dateFormat, time.localtime(randomTime))
    return randomDate

print("Random Date = ", getRandomDate("5/10/2030", "30/10/2034"))
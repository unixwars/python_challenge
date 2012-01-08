#!/usr/bin/env python
#title: whom?
#hint1: leap year, between 1906 and 1996, Jan 26 was Monday
#hint2: he ain't the youngest, he is the second
#hint3: todo: buy flowers for tomorrow
#fact1: birth day is Jan 27
import datetime,calendar
for year in range(1006,1996,10):
    d=datetime.date(year, 1, 26)
    if d.isoweekday() == 1 & calendar.isleap(year):
        print d

##1176-01-26
##1356-01-26
##1576-01-26    
##1756-01-26    <---- this one is the second most recent. He was born 1756-01-27. mozart.html (says Wikipedia)
##1976-01-26

#mozart.html

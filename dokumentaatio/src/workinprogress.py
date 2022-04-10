from datetime import date, datetime, timedelta

Syear = 2022
Smonth = 5
Sday = 15
Eyear = 2022
Emonth = 6
Eday = 14

start = date(Syear, Smonth, Sday)
end = date(Eyear, Emonth, Eday)

class Budget2:
    def setBudget(self):
        length = int(end - start)
        print(length)
        
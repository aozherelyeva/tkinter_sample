import calendar
from datetime import datetime
cal = calendar.TextCalendar(calendar.MONDAY)
currentMonth = datetime.now().month
currentYear = datetime.now().year
f_calendar = cal.formatmonth(currentYear, currentMonth)
print(f_calendar)
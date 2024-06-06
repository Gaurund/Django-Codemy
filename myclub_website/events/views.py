import calendar
from calendar import HTMLCalendar
from datetime import datetime

from django.shortcuts import render


def home(request, year, month):
    name = "John"
    month = month.title()
    month_number = list(calendar.month_name).index(month)
    month_number = int(month_number)

    cal = HTMLCalendar().formatmonth(year, month_number)

    now = datetime.now()
    current_year = now.year

    time = now.strftime('%H:%M:%S %p')
    return render(
        request,
        'home.html',
        {
            'name': name,
            'year': year,
            'month': month,
            'month_number': month_number,
            'cal': cal,
            'current_year': current_year,
            'time': time,
        }
    )

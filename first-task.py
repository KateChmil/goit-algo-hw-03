from datetime import datetime


def get_days_from_today(date):
    try:
        given_date = datetime.strptime(date, "%Y-%m-%d")
        today = datetime.today()

        difference = today.date() - given_date.date()
        print(f"Кількість днів до {today.date()}: {difference.days}")
        return difference.days
    except ValueError:
        return "Invalid date format"

 
get_days_from_today("2026-09-14")
get_days_from_today("2026-09-17")

from datetime import datetime

def get_days_from_today(date) -> int:
    try:
        date = datetime.strptime(date,  "%Y-%m-%d").date()
        today = datetime.today().date()
        return (today - date).days
    except ValueError:
        return "Invalid date format. Please use YYYY-mm-dd."

date = input("Enter a date in YYYY-mm-dd format: ")
print(get_days_from_today(date))
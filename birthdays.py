from datetime import datetime, timedelta


users_list = [
{'name': 'Alex', 'birthday': datetime(year=2022, month=10, day=1)},
{'name': 'Lily', 'birthday': datetime(year=2022, month=9, day=25)},
{'name': 'Stasy', 'birthday': datetime(year=2022, month=9, day=27)},
{'name': 'Mia', 'birthday': datetime(year=2022, month=9, day=29)},
{'name': 'Bella', 'birthday': datetime(year=2022, month=9, day=26)},
{'name': 'Violetta', 'birthday': datetime(year=2022, month=9, day=30)},
{'name': 'Emma', 'birthday': datetime(year=2022, month=10, day=5)},
{'name': 'Susan', 'birthday': datetime(year=2022, month=10, day=3)},
{'name': 'Anna', 'birthday': datetime(year=2022, month=10, day=2)},
{'name': 'Regena', 'birthday': datetime(year=2022, month=10, day=4)}
]

def get_birthdays_per_week(users: list):
    result_list = {
        "Monday": [],
        "Tuesday": [],
        "Wednesday": [],
        "Thursday": [],
        "Friday": []
    }

    now_day = datetime.now()
    days_interval = define_days_interval(now_day)
    new_time_line = now_day + days_interval

    for user in users:
        name = user['name']
        birthday = datetime(
            year=now_day.year,
            month=user.get('birthday').month,
            day=user.get('birthday').day
        )
        if now_day < birthday <= new_time_line:
            weekday = birthday.strftime("%A")
            if weekday in ['Saturday', 'Sunday']:
                weekday = 'Monday'
            result_list[weekday].append(name)
    print_users_list(result_list)


def define_days_interval(now_day: datetime) -> timedelta:
    if now_day.weekday() == 5:
        days_interval = timedelta(days=6)
    elif now_day.weekday() == 6:
        days_interval = timedelta(days=5)
    else:
        days_interval = timedelta(days=7)

    return days_interval

def print_users_list(users_list: dict):
    for key, value in users_list.items():
        if value:
            print(f"{key}: {', '.join(value)}")

if __name__ == '__main__':
    get_birthdays_per_week(users_list)


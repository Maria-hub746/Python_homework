from datetime import datetime
import calendar


def get_birthdays_per_week(users):
    result = {'Monday': [],
        'Tuesday':[],
        'Wednesday' : [],
        'Thursday' : [],
        'Friday' : []
    }

    today_now = datetime.now()
    for user in users:
        name = user['name']
        birthday = user['birthday']
        difference = birthday - today_now
        difference = difference.days
        if difference < 7:
            week = birthday.strftime('%A')
            if week == 'Saturday' or week == 'Sunday':
                week = 'Monday'
                result[week].append(name)
                
            else:
                result[week].append(name)
                
    return result
                

                    


            

user = [
{'name': 'Alex', 'birthday': datetime(year=2022, month=10, day=1)},
{'name': 'Lily', 'birthday': datetime(year=2022, month=9, day=25)}
]

print(get_birthdays_per_week(user))
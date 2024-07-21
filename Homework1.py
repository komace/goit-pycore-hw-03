from datetime import datetime

def get_days_from_today(date):
    # використовуємо try , except  для обробки неправильного формату вхідних даних
    try:
        # перетворення рядка дати у обєкт datetime
        date = datetime.strptime(date, "%Y-%m-%d")

        # отримання поточної дати 
        date_now = datetime.today()

        # розрахунок різниці між поточною датою і заданою датою
        diference_days = date_now - date

        # повернення різниці у днях як ціле число
        return diference_days.days
    except ValueError:
        # обробкa неправильного формату вхідних даних
        return 'Invalid date format, please enter correct date "YYYY-MM-DD"! '
    
# приклад використання функції    
print(get_days_from_today("1198-10-09"))
print(get_days_from_today("0298-10-09"))
print(get_days_from_today("398-122-09"))
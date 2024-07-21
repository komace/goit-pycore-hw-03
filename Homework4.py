from datetime import datetime, timedelta

def get_upcoming_birthdays(users: list[dict]) -> list[dict]:
    # визначаємо поточну дату
    today = datetime.today().date()
    # обчислюємо дату яка буде через 7 днів за допомогою класу timedelta
    next_week = today + timedelta(days=7)
    # задаємо зміну пусту
    upcoming_birthdays = []
    
    # використовуємо цикл для перевірки днів народження
    for user in users:
        # перетворюємо дату народження з рядка у обєкт за допомогою методу "strptime"
        birthday = datetime.strptime(user['birthday'], '%Y.%m.%d').date()
        # змінюємо рік народження на теперіщній рік, для подальщого обчислення днів
        birthday_this_year = birthday.replace(year=today.year)
        
        # якщо ДР вже минув цього року, використовуємо дату наступного року
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)
       
        # перевіряємо чи ДР у межах наступного тижня
        if today <= birthday_this_year <= next_week :
            # якщо ДР припадає на вихідний, переносимо на наступний понеділок
            if birthday_this_year.weekday() >= 5:
                # знаходимо наступний понеділок
                days_to_monday = 7 - birthday_this_year.weekday()
                birthday_this_year += timedelta(days=days_to_monday)
            # додаємо результат до списку
            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": birthday_this_year.strftime("%Y.%m.%d")             
            })
    return upcoming_birthdays        
users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1970.01.27"},
    {"name": "Boe Jiden", "birthday": "1982.07.24"},
    {"name": "Tonald Drump", "birthday": "1963.07.25"},
    {"name": "Stu Kenny", "birthday": "1974.07.26"},
    {"name": "Eve Blue", "birthday": "1995.07.27"},
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:",upcoming_birthdays)
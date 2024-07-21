import random

def get_numbers(min , max , quantity ):
    # перевірка коректності вхідних параметрів
    if min < 1 or max > 1000 or quantity < 0:
        return[]
    
    # генерація унікальних випадкових чисел
    number = random.sample(range(min, max),quantity)
    # повернення відсортованого списку унікальних чисел
    return sorted(number)

# використання функції з заданими параметрами
lottery_numbers = get_numbers(1,49,6)
print(lottery_numbers)
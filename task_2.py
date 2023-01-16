#Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения,
#город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных
#о пользователе одной строкой.

name = input('enter name ')
surname = input('enter surname ')
year = int(input('enter year '))
city = input('enter city ')
email = input('enter email ')
telephone = input('input telephone ')

def my_func (name, surname, year, city, email, telephone):
    return ' '.join([name, surname, year, city, email, telephone])
print(my_func(surname = 'Бондаревич', name = 'Евгений', year = '1984', city = 'Москва', email = 'bondarevich32@yandex.ru', telephone = '89800000000'))
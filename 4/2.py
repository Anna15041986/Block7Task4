"""
2. Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.

Пример:
Иван Иванов 1846 года рождения, проживает в городе Москва, email: jackie@gmail.com, телефон: 01005321456
"""


def print_user(name, surname, birth_year, city_of_residence, email, phone):
    print(
        f"{name} {surname} {birth_year} года рождения, проживает в городе {city_of_residence}, "
        f" email: {email}, телефон: {phone}")
user = {
    "name": "Имя",
    "surname": "Фамилия",
    "birth_year": "Год рождения",
    "city_of_residence": "Город проживания",
    "email": "Email",
    "phone": "Телефон"
}
user_data = {}
for key, value in user.items():
    input_value = input(f'{value}: ')
    user_data.update({key: input_value})
print_user(**user_data)

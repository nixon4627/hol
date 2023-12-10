def hello_who(name):
    return f'Hello,{name}'

def salary(hours,salary_by_hours):
    '''
    Рассчёт зп сотрудника
    :param hours: количество часов
    :param salary_by_hours: зарплата за час
    :return: итоговая сумма
    '''
    k = 2
    return hours * salary_by_hours * k
print(2)
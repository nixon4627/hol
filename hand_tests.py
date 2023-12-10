from functions import salary,hello_who

print(hello_who('Max'))

print(salary(hours=2,salary_by_hours=10))

if salary(hours=2,salary_by_hours=10) != 40:
    print('Error')
if hello_who('Max') != 'Hello,Max':
    print('Failed')
else:
    print('Good')
if hello_who('Leo') != 'Hello,Leo':
    print('Failed')
else:
    print('Amazing')

print(hello_who('Amanda'))

print(salary(hours=5,salary_by_hours=5))

if salary(hours=5,salary_by_hours=5) != 50:
    print('Error')
if hello_who('Amanda') != 'Hello,Amanda':
    print('Failed')
else:
    print('Good')
if hello_who('Alex') != 'Hello,Alex':
    print('Failed')
else:
    print('Amazing')
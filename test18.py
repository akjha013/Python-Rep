# exceptions and errors
try:
    age = int(input('Age: '))
    income = 20000
    risk = income/age
    print(age)

except ValueError:
    print('Err: Invalid value')
except ZeroDivisionError:
    print('Err: Age cannot be 0')

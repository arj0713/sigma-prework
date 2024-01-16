from datetime import datetime

def age(date):
    date = datetime.strptime(date, '%d-%m-%Y')
    current_date = datetime.now()

    time_difference = current_date - date
    age = time_difference.days // 365

    return age

#option for pre specified date or user input
date = '01-01-2014'
#date = input("What date would you like to calculate age from? ")

age = age(date)
print(f"The age from {date} is {age} years")

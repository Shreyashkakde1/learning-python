### Dictionaries ##

# Note: Dictionaries are Mutable(change-able / update-able)

# key -> value

person = {'name': 'Shreyash',
          'Surname': 'Kakde',
          'Phone': '7796-74-3579',
          'Age': 20,
          'Hight': 5.9,
          'assets': 100,
          'debt': 50,
          'netWorth': lambda : person['assets'] - person['debt']
        }


print(person['name'])
print(person['Surname'])
print(person['Age'])
print(person['Hight'])
print(person['netWorth']()) # while calling the lamda function end the () 

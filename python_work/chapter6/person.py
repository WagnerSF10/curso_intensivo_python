person = {
    'first_name': 'wagner',
    'last_name': 'de souza frança',
    'age': 38,
    'city': 'campinas',
    }

age = person['age']

print("My name is " + person['first_name'].title() + " " + 
    person['last_name'].title() + ", I'm " + str(age) + 
    " years old and I live in " + person['city'] + "!")

###Intruções if
cars=['audi','bmw','subaru','toyota']
for car in cars:
    if car =='bmw':
        print(car.upper())
    else:
        print(car.title())
###Verificando igualdade
# >>> car='bmw'
# >>> car=='bmw'
# True
# >>> car='audi'
# >>> car=='bmw'
# False

###Ignorando as diferenças entre letras maiusculas e minusculas a verificar a igualdade.
# >>> car='Audi'
# >>> car=='audi'
# False
# >>> car='Audi'
# >>> car.lower()=='audi'
# True


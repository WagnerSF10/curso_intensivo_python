car='subaru'
print("\nIs car == 'subaru'? I predict True.")
print(car=='subaru')

print("\nIs car == 'audi'? I predict False.")
print(car=='audi')

#       _____//______

age=35
if age==35:
    print("\nIdade 35? Eu direi True.")
    print(age==35)
else:
    print("\nIdade 35? Eu direi False.")
    print(age!=35)

#       _____//______

age=37
print("\n" + str(age))
if (age<=34) or (age<=41):
    print("Age is >=35 or <=41?")
    print(age==37)
else:
    print(age==37)

#       _____//______

age='trinta_e_oito'
print("\n\nMInha Idade==38? True!")
print(age=='trinta_e_oito')

print("Minha Idade !=38? False.")
print(age=='qualquer')

#       _____//______

cars=['corola','fiat','chevrolet']
for car in cars:
    if car=='corola':
        print(car.title())
    else:
        print(car!=car)

#       _____//______

name='juliana'
if name=='juliana':
    print("\nNome presente na familia: "+name)
else:
    print("\nCasada.")

#       _____//______

names=['eliezer','rute','wagner']
for name in names:
    if name=='wagner':
        print("\n"+ str(name.title()))
    else:
        print("\n"+ str(name.upper()))

#       _____//______

age_0=18
age_1=20
if age_0==18 and age_1==20:
    print("\n"+str(age_0==age_1))
else:
    print(age_0)
    print(age_1)

#       _____//______

age_0=18
age_1=20
if age_0==20 or age_1==20:
    print("\n"+str(age_0!=age_1))
else:
    print(age_0)
    print(age_1)

#       _____//______

age_0=18
age_1=20
if age_0==20 or age_1==18:
    print("\n"+str(age_0!=age_1))
else:
    print("\n"+str(age_0))
    print("\n"+str(age_1))

#       _____//______

relatives=['eliezer','rute','wagner']
relative='rute'
if relative in relatives:
    print("\n"+relative.title()+ " eh da familia!")

relatives=['eliezer','rute','wagner']
relative='desconhecido'
if relative not in relatives:
    print(relative.title()+ ", a qual familia voce pertence?")
    

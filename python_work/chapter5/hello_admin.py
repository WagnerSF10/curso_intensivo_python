names=['eliezer', 'rute', 'priscila', 'juliana', 'wagner', 'admin']
for name in names:
    print(name.title() + "! Bem vindo(a)!")
    if name=='admin':
        print("Olá " + name.title() + ", gostaria de ver um relatório de status?")
    else:
        print("Olá " + name.title() + ", obrigado por fazer um login novamente.")

#Sem usuários
names=[]
if names==[]:
    print("Precisamos encontrar alguns usuários!")
else:
    ("Há usuários cadastrados!")

#Verificando nomes de usuários com validações
current_users = ['eliezer', 'rute', 'priscila', 'juliana', 'WAGNER', 'admin']
new_users = ['felipe', 'gustavo', 'anne', 'Wagner', 'admin']
for new_user in new_users:
    if new_user in current_users:
        print(new_user + "\nPor favor, forneça outro nome.")
    else:
        print(new_user + "\nEste nome de usuário está disponível.")

#Exibindo terminações de números ordinais
ordinal_numbers = [1,2,3,4,5,6,7,8,9]
for ordinal_number in ordinal_numbers:
    if ordinal_number == 1:
        print(str(ordinal_number) + "st")
    elif ordinal_number == 2:
        print(str(ordinal_number) + "nd")
    elif ordinal_number == 3:
        print(str(ordinal_number) + "rd")
    else:
        print(str(ordinal_number) + "th")


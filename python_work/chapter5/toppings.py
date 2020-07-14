###Verificando a diferenca
requested_topping='mushrooms'
if requested_topping != 'anclvies':
    print("Hold the anchovies!\n\n")

###Comparacoes numericas
# >>> age=18
# >>> age==18
# True

###Testando varias condicoes
requested_toppings=['mushrooms','extra cheese']
if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")
print("\nFinished making your pizza!\n\n")

###Verificando itens especiais
requested_toppings=['mushrooms','green peppers','extra cheese']
for requested_topping in requested_toppings:
    print("Adding " + requested_topping + ".")
print("\nFinishedmaking your pizza!\n\n")

###Verificando itens especiais = ausencia de pimentoes verdes
requested_toppings=['mushrooms','green peppers','extra cheese']
for requested_topping in requested_toppings:
    if requested_topping=='green peppers':
        print("Sorry, we are out o green peppers right now.")
    else:
        print("Adding " + requested_topping + ".")
print("\nFinished making your pizza!\n\n")

###Verificando se uma lista nao esta vazia
requested_toppings=[]
if requested_toppings:
    for requested_topping in requested_toppings:
        print("Adding " + requested_topping + ".")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?\n\n")    
    
###Usando varias listas
available_toppings=['mushrooms','olives','green peppers','pepperoni','pineapple','extra cheese']
requested_toppings=['mushrooms','french fries','extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding " + requested_topping + ".")
    else:
        print("Sorry, we don't have " + requested_topping + ".")    
print("\nFinished making your pizza!")        

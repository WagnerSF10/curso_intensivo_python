my_pizzas=['parmegiana','frango','portuguesa','margaritta','bacon']
friend_pizzas=my_pizzas[:]

my_pizzas.append('cogumelos')

friend_pizzas.append('atum')

print("Minhas pizzas favoritas sao:")
for my_pizza in my_pizzas:
	print(my_pizza.title())

print("\nAs pizzas favoritas do meu amigo sao:")
for friend_pizza in friend_pizzas:
	print(friend_pizza.title())

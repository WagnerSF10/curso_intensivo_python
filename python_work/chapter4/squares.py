

squares=[] #Criacao de lista dos dez primeiros quadrados perfeitos ( 1 a 10)
for value in range(1,11):
	square=value**2
	squares.append(square)
print(squares)

squares=[] #Forma concisa de criação de quadrados perfeitos (1 a 10)
for value in range(1,11):
	squares.append(value**2)
print(squares)

# >>> digits=[1,2,3,4,5,6,7,8,9,0]
# >>> min(digits)
# 0
# >>> max(digits)
# 9
# >>> sum(digits)
# 45
# >>>

squares=[value**2 for value in range(1,11)]
#List comprehensions (abrangencia da lista) gera com apenas um linha de código a mesma lista.
print(squares)

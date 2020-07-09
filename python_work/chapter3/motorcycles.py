motorcycles=['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0]='ducati'						#Modifica uma lista
print(motorcycles)
motorcycles=['honda', 'yamaha', 'suzuki']
motorcycles.append('ducati') 				#Acrescenta elementos no final da lista sem alterar outros elementos
print(motorcycles)
motorcycles=['honda', 'yamaha', 'suzuki']
motorcycles.insert(0,'ducati')				#Adiciona qualquer elemento em qualquer posição da lista
print(motorcycles)
motorcycles=['honda', 'yamaha', 'suzuki']
del motorcycles[0]							#Remove itens de posições conhecidas
del motorcycles[1]
print(motorcycles)
motorcycles=['honda', 'yamaha', 'suzuki']
print(motorcycles)
popped_motorcycles=motorcycles.pop()		#Remove o ultimo item da lista que eh reutilizavel
print(motorcycles)
print(popped_motorcycles)

motorcycles=['honda', 'yamaha', 'suzuki']
first=motorcycles.pop(0)					#Remove o item desejado de uma lista
print(first)

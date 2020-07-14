###Tuplas - criam listas de itens que nao sao mutaveis - listas imutaveis
dimensions=(200,50)
print(dimensions[0])
print(dimensions[1])
#dimensions[0]=250

###Percorrendo todos os valores de uma tupla com um laco
for dimension in dimensions:
	print(dimension)

###Sobrescrevendo uma tupla
dimensions=(200,50)
print("\n\n\nOriginal dimensions:")
for dimension in dimensions:
	print(dimension)

dimensions=(400,100)
print("\n\n\nModified dimensions:")
for dimension in dimensions:
	print(dimension)

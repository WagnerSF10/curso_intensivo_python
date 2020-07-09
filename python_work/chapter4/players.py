players=['charles','martina','michel','florence','eli']
print(players[0:3])#Exibe os tres primeiros itens da lista

players=['charles','martina','michel','florence','eli']
print(players[1:4])#Sao exibidos os itens segundo ao terceiro

players=['charles','martina','michel','florence','eli']
print(players[:4])#Sao exibidos os itens primeiro ao terceiro

players=['charles','martina','michel','florence','eli']
print(players[2:])#Sao exibidos os itens terceiro ao ultimo

players=['charles','martina','michel','florence','eli']
print(players[-3:])#Sao exibidos os tres ultimos itens da lista

players=['charles','martina','michel','florence','eli']
print("\nHere are the first three players on my team:")
for player in players[:3]:
#Laço for para percorrer os tres primeiros itens da lista
	print(player.title())


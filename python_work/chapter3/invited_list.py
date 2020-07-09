invited=['eliezer','rute','esposa','priscila','juliana']
print(invited)
message=", vamos jantar?!"
invited_message0="\n" + invited[0].title() + message
invited_message1=invited[1].title() + message
invited_message2=invited[2].title() + message
invited_message3=invited[3].title() + message
invited_message4=invited[4].title() + message
print(invited_message0 + "\n" + invited_message1+ "\n" + invited_message2)
print(invited_message3 + "\n" + invited_message4)
print("\nTodos os convidados, a " + invited[3].title() + " nao conseguira estar presente.\n")
third_invited=invited.pop(3)
invited.insert(3,'avo')
invited_message5=invited[3].title() + message + " Pois a " + third_invited.title() + " não estara presente!\n\n"
print(invited_message5)
print(invited)
big_table="\nConsegui uma mesa para 8 pessoas. Vou convidar mais 3 pessoas!!\n"
print(big_table)
invited.insert(0,'cunhado')
invited.insert(2,'sogra')
invited.append('sogro')
print(invited)
new_message=", voce aceita jantar conosco?!\n"
invited_message00=invited[0].title() + new_message
invited_message01=invited[1].title() + new_message
invited_message02=invited[2].title() + new_message
invited_message03=invited[3].title() + new_message
invited_message04=invited[4].title() + new_message
invited_message05=invited[5].title() + new_message
invited_message06=invited[6].title() + new_message
invited_message07=invited[7].title() + new_message
print(
	"\n"+invited_message00+
	"\n"+invited_message01+
	"\n"+invited_message02+
	"\n"+invited_message03+
	"\n"+invited_message04+
	"\n"+invited_message05+
	"\n"+invited_message06+
	"\n"+invited_message07)
more_message="\nPuxa, a nova mesa nao chegara a tempo!\n\nSoh haverah lugar para duas pessoas infelizmente.\n\n"
print(more_message)
popped_invited=invited.pop(7)
print(popped_invited.title() + ", desculpe, mas voce nao poderah jantar comigo!\n")
popped_invited=invited.pop(6)
print(popped_invited.title() + ", desculpe, mas voce nao poderah jantar comigo!\n")
popped_invited=invited.pop(5)
print(popped_invited.title() + ", desculpe, mas voce nao poderah jantar comigo!\n")
popped_invited=invited.pop(3)
print(popped_invited.title() + ", desculpe, mas voce nao poderah jantar comigo!\n")
popped_invited=invited.pop(2)
print(popped_invited.title() + ", desculpe, mas voce nao poderah jantar comigo!\n")
popped_invited=invited.pop(1)
print(popped_invited.title() + ", desculpe, mas voce nao poderah jantar comigo!\n")
popped_invited=invited.pop(0)
print(popped_invited.title() + ", desculpe, mas voce nao poderah jantar comigo!\n")
print(invited[0].title() + ", soh nos dois jantaremos!\n")
del invited[0]
print(invited)
# >>> invited=['eliezer','rute','esposa','priscila','juliana']
# >>> len(invited)
# 5
# >>>

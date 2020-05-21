print("""
--------------
| \033[36mRCovery :)\033[m |
--------------
\033[1mModo de usar: Nomes, Siglas, Datas (01/02/1234), Números, Etc...\033[m
""")
list_resp = list() #Respostas
new_list = list() #Wordlist
new = "."
while not new == "":
	new = input("$ Keyword (press enter to stop):: ")
	try:
		if "/" in new:
			newCorrection = new.replace("/", " ").split() #Remove as barras da data e separa a string

			for elements in newCorrection:
				list_resp.append(elements)
		else:
			newCorrection = new.split()
			for element in newCorrection:
				list_resp.append(element)

	except Exception as error:
		print(error)

for a in list_resp: #Mistura os elementos
	for b in list_resp:
		for c in list_resp:
			new_list.append(a+b+c)
		new_list.append(a+b)
	new_list.append(a)

print("\n$ Foram geradas {} senhas.\n".format(len(new_list)))

wordlist = open("wordlist.dat","w")
for words in new_list:
	wordlist.write(words+'\n')
wordlist.close()

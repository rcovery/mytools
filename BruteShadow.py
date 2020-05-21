import crypt
from sys import argv
print("""
--------------
| \033[32mRcovery ;ç\033[m |
--------------
""")
try:
	salt = '$6$xxqElE.8Afl/qcX9$' #Put the salt
	_pass = '$6$xxqElE.8Afl/qcX9$Zu/Xv/3kLEHBpMJuSSxcN5c0JYomtKGgUL4hIYjnT1stevkwlhghQF5.woohAYnEOQPNuSzASYbcUNVMmqaXa0' #Put the password salted

	_wordlist = open(argv[1],"r").read().split() #Put the wordlist file in the arguments

	for item in _wordlist:
		newPass = crypt.crypt(item,salt)
		if (newPass == _pass):
			print(f"\033[32mThe password is: \033[1;35m{item}\033[m")
			break
		else:
			pass
except IndexError:
	print("""\033[32m<-Modo de usar->
\033[1mpython3 BruteShadow.py file\033[m
""")
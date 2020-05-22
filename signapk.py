from os import system
from sys import argv

print("""\033[36m
--------------
| RCovery :( |
--------------\033[m
""")

#you must install keytool to generate key
#you must install jdk to use jarsigner and sign apk

try:
	_filename = argv[1]

	generateKey = "keytool -genkey -keystore debug.keystore -storepass android -alias androiddebugkey -keypass android -keyalg RSA -keysize 2048 -validity 10000"
	signApk = "jarsigner -keystore debug.keystore -storepass android -keypass android -digestalg SHA1 -sigalg MD5withRSA {} androiddebugkey".format(_filename)

	system(generateKey)
	print("[!] Key generated")
	system(signApk)
	print("[!] APK Signed")
except IndexError:
	print("""\033[32m<-How to use->
\033[1mpython3 signapk.py yourapk.apk\033[m
""")


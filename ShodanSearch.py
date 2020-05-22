import shodan
from sys import argv

print("""\033[1;35m
·-·-·-·-·-·-·
| RCovery :>|
·-·-·-·-·-·-·\033[m
""")

api_key = "" #Insert the shodan API key
s = shodan.Shodan(api_key)

try:
	resultado = s.search(argv[1])
	r = resultado['matches']
	for result in r:
		print("""------------------------
	IP: {}
	PORT: {}
	HOSTNAME: {}
	SO: {}""".format(result['ip_str'], result['port'], result['hostnames'], result['os']))
except IndexError:
	print("""\033[1;32m<-How to use->
\033[0;32mpython3 ShodanSearch.py IP\033[m
""")

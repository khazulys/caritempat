import requests, json
import os
from time import sleep

def main():

	try:
		api_key = 'AIzaSyChq3CxzQwiXbCmqXHvO4cuMjQKXiwoutg'
		url = "https://maps.googleapis.com/maps/api/place/textsearch/json?"
		query = input('\n\033[1;35m[+]\033[1;36mCari tempat:\033[1;32m ')
		print ("\033[1;35m[+]\033[1;36mMembuka google maps\n")
		sleep(3)
		r = requests.get(url + 'query=' + query +
        		                '&key=' + api_key)
		x = r.json()
		y = x['results']
		for i in range(len(y)):
		    print("\033[1;31m[+]\033[1;33mResult:\033[1;36m ", y[i]['name'])


		while True:
			ul = input("\n\033[1;34m[?]\033[1;31mMau nyari lagi?(y/n):\033[1;33m ")
			if ul =="y":
				main()
			elif ul =="n":
				exit("GoodBye")

	except:
		pass

if __name__ == "__main__":
	#banner
	os.system('cls' if os.name == "nt" else 'clear')
	print ("\033[1;32m	╔═╗┌─┐┬─┐┬  ╔╦╗┌─┐┌┬┐┌─┐┌─┐┌┬┐ ")
	print ("\033[1;35m	║  ├─┤├┬┘│   ║ ├┤ │││├─┘├─┤ │ ")
	print ("\033[1;32m	╚═╝┴ ┴┴└─┴   ╩ └─┘┴ ┴┴  ┴ ┴ ┴ ")
	print ("\033[1;36m	  Cari tempat nongkrong yuks ")
	print ("\033[1;34m	   [+]\033[1;33mCoded By Khazul\033[1;34m[+]")


	main()

import secrets
from os import system

system('title PassWord Generator')
system('color a')
system('cls')

print("""______             _    _               _   _____                           _             
| ___ \           | |  | |             | | |  __ \                         | |            
| |_/ /_ _ ___ ___| |  | | ___  _ __ __| | | |  \/ ___ _ __   ___ _ __ __ _| |_ ___  _ __ 
|  __/ _` / __/ __| |/\| |/ _ \| '__/ _` | | | __ / _ \ '_ \ / _ \ '__/ _` | __/ _ \| '__|
| | | (_| \__ \__ \  /\  / (_) | | | (_| | | |_\ \  __/ | | |  __/ | | (_| | || (_) | |   
\_|  \__,_|___/___/\/  \/ \___/|_|  \__,_|  \____/\___|_| |_|\___|_|  \__,_|\__\___/|_|   
                                                                                          
                                                                                          """)

try:
	caracter = int(input('choose a number of characters >'))
	print('*'*50)
	print("\t", secrets.token_urlsafe(caracter))
	print('*'*50)
except ValueError:
	system('cls')
	print('\n\tYou must use a number !!!')
	exit(0)
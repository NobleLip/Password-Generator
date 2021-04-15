import random 

Special = 'abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?'
Char = 'abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ'

PasswordSpecial = input('Special Characters? Y/N\n')
Password_Comprimento= int(input('Legth of Password?\nR:'))
Password_Number=int(input('Number of Passwords?\nR:'))


if PasswordSpecial.lower() == 'n':
	for Passwords in range(Password_Number):
		Pass = '' 
		for Letra in range(Password_Comprimento):
			Pass = Pass + random.choice(Char)
		print(str(Passwords+1) + (len(str(Password_Comprimento+1)) - len(str(Passwords+1))) * ' ' + ': '+ Pass)

else:
	for Passwords in range(Password_Number):
		Pass = '' 
		for Letra in range(Password_Comprimento):
			Pass = Pass + random.choice(Special)
		print(str(Passwords+1) + (len(str(Password_Comprimento+1)) - len(str(Passwords+1))) * ' ' + ': '+ Pass)
country = input('請輸入國家')
age = input('請輸入年齡')
age = int(age)
if country == 'Taiwan':
	if age >= 18:
		print('你可以考駕照')
	else:
		print('你還不能考駕照')
elif country == 'US':
	if age >= 16:
		print('你可以考駕照')
	else:
		print('你還不能考駕照')

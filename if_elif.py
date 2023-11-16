age = input("請輸入年齡: ")
age = int(age)
if age <= 13:
	print('你是小學生(含以下)')
elif age > 13 and age <= 18:
	print('你是國高中生')
elif age > 18 and age <= 22:
	print('你是大學生')
elif age > 22 and age <= 65:
	print('你是社會人士')		
else:
	print('你退休了')				
import random

while True:
	try:
		star = input('請輸入開始範圍')
		end = input('請輸入結束範圍')
		star = int(star)
		end = int(end)
		break
	except (TypeError, ValueError) as e:
		print('輸入錯誤:只能輸入整數, 請重啟')
		
true_number = random.randint(star,end)

count = 0
while True:		
	user_number = int(input('請輸入數字: '))
	count += 1

	if user_number < true_number:
		print('比正確答案小')
	elif user_number > true_number:
		print('比正確答案大')
	elif user_number == true_number:
		print('bengo!答對瞜!')
		print('你已經輸入', count, '次!')	
		break		

	print('你已經輸入', count, '次!')		



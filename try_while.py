#用迴圈讓使用者選擇 模式1/模式2/模式3/  或跳出迴圈 q離開



while True:
	mode = input('請輸入遊戲模式1/2/3, 離開輸入q : ')
	if mode == 'q':
		break
	elif mode == '1':
		print('模式1')
	elif mode == '2':
		print('模式2')
	elif mode == '3':
		print('模式三')	
	else:
		print('請輸入1/2/3/q')

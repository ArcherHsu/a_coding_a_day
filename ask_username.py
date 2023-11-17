#目標 使用者可以不斷輸入名子
#且 輸入Q可以離開
ask_times = 0
while True:	
	if ask_times < 1:
		user_name = input('請問你的名子  或者 輸入 q 離開: ')
		ask_times += 1
	elif ask_times >= 1 and ask_times < 3:
		user_name = input('輸入你的名子 或者 輸入 q 離開: ')
		ask_times += 1
	elif ask_times >= 3 and ask_times < 4:
		user_name = input('好了我知道了, 你叫做' + user_name + ', 再說就翻臉! : ')	
		ask_times += 1
	if user_name == 'q' or ask_times>=4:
		break
	else:	
		print('你好', user_name)	
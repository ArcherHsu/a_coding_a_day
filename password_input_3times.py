password = 'a123456'
userinput = input('請輸入密碼: ')
i = 3
while i>0:
	if password == userinput:		
		break
	else:
		t = str(i)
		userinput =input('輸入錯誤,你還有'+t+'次機會!: ')	
	i -= 1	
if userinput == password: 
	print('登入成功!, 登入手續費50%!')
else:	
	print('由於帳號連續錯誤次數過多,你的銀行帳號已經自動消滅!')
		
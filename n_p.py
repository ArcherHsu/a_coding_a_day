arr = []
while True:
	name = input('請輸入商品名稱')
	if name=='Q' or name=='q':
		break
	price = input('請輸入商品價格')
	if price =='Q' or price =='q':
		break	
	n_p = [name, price]
	arr.append(n_p)
print(arr)

with open('n_p.txt','w') as f:
	for i in arr:
		f.write(str(i[0])+'的價格為'+str(i[1])+'\n')
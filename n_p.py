#讀取檔案
arr = []
with open('n_p2.csv', 'r') as f:
	for line in f:
		if '商品,價格' in line:
			continue
		s=line.strip().split(',')
		arr.append(s)
print(arr)


#使用者輸入
while True:
	name = input('請輸入商品名稱')
	if name=='Q' or name=='q':
		break
	price = input('請輸入商品價格')
	if price =='Q' or price =='q':
		break	
	n_p = [name, price]
	arr.append(n_p)


#存檔
with open('n_p2.csv','w') as f:
	f.write('商品,價格\n')
	for i in arr:
		f.write(str(i[0])+','+str(i[1])+'\n')
print(arr)		

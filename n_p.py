import os

the_file = 'n_p3.csv' #檔案名稱
arr = []

#檢查檔案
if os.path.isfile(the_file): 
	print('載入檔案', the_file)	
	with open(the_file, 'r') as f: #讀取檔案
		for line in f:
			if '商品,價格' in line:
				continue
			s=line.strip().split(',')
			arr.append(s)
		print(arr)	
else:
	print('無法找到檔案', the_file, '將新增新檔')	

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
with open(the_file,'w') as f: 
	f.write('商品,價格\n')
	for i in arr:
		f.write(str(i[0])+','+str(i[1])+'\n')
print(arr)		

#讀取txt在所有資料只讀100筆並且印出前2筆
#發想來於有一筆資料足足300M大
data = []
i = 0
with open('reviews.txt', 'r') as f:
	for i in range(100):
		line = f.readline()		
		data.append(line.strip())
		
print(len(data))		
print(data[0])
print('-------------')
print(data[1])
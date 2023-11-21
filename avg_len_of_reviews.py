data = []
count = 0
number = 0
low = []
good = []
with open('reviews.txt', 'r') as f:
    for line in f:
        count += 1
        data.append(line)
        number += len(line) 
for i in data:
    if len(i) < 100:
        low.append(i)
    if "good" in i:
        good.append(i)  

avg = number / len(data)

print('共讀取', count, '筆資料')
print('所有留言平均字數為', avg,'個字母')

print('字母數小於100的流言有', len(low), '筆')
print('有',len(good),'筆資料裡面含good字眼')

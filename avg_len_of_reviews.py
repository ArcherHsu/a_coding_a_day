data = []
count = 0
number = 0
with open('reviews.txt', 'r') as f:
    for line in f:
        count += 1
        data.append(line)
        number += len(line)
        
avg = number / len(data)
print(avg)
print(count)

#所有字數/長度
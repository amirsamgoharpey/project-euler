number = 1
for i in range(1,101):
    number = i*number
sum = 0
for i in str(number):
    sum = sum + int(i)
print(sum)

## 648
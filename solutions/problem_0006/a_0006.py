square = 0
sum = 0
for i in range(1 , 101) :
    sum = sum + i
    square = square + i**2

print(sum**2 - square)

largest = 1
numberin = 0
for i in range(1,1000000):
    large = 1
    number = i
    while i != 1:
        if i%2 == 0 :
            i = i/2
        else:
            i = 3*i+1
        large = large + 1
    if large > largest :
        largest = large
        numberin = number

print(largest)
print(numberin)

## 837799
seq_1 = 1
seq_2 = 2
sum = 0
while seq_2 < 4000000: 
    if seq_2%2 == 0 :
        sum = sum + seq_2
    elif seq_1%2 == 0 :
        sum = sum + seq_1
    seq_1 = seq_1 + seq_2
    seq_2 = seq_2 + seq_1
print(sum)

## 4613732

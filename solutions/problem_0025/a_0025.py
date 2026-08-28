import time
seq_1 = 1
seq_2 = 2
sum = 0
while len(str(seq_2)) != 1000: 
    if seq_2%2 == 0 :
        sum = sum + seq_2
    elif seq_1%2 == 0 :
        sum = sum + seq_1
    seq_1 = seq_1 + seq_2
    seq_2 = seq_2 + seq_1
    print(seq_2)
    time.sleep(0.2)

## 4613732

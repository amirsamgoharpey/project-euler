import time
primes = [2]
position = 2
while True :
    state = True
    for i in primes:
        if position%i == 0 :
            state = False
    if state :
        primes.append(position)
    position = position + 1
    try:
        print(primes[10000])
        break
    except:
        continue

## 104743

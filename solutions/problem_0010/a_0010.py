import time
primes = [2]
position = 2
#f = open("prime.txt", "w")
#f.write("1 = 2 \n")
start = time.time()
while True :
    state = True
    for i in primes:
        if position%i == 0 :
            state = False
    if state :
        if position > 200000:
            break
        else:
            primes.append(position)
                #f.write(str(primes.index(position)+1) + " = " + str(position) + "\n")
    position = position + 1
stop = time.time()
print(sum(primes))
print(stop-start)

## 142913828922 , it took me more than 3 hours to get to answer!
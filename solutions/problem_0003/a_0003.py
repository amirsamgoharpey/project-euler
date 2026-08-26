import time
number = 600851475143
factors = []
state = 0
start = time.time()
for i in range(number) :
    if number%(i+1) == 0:
        for j in factors:
            if j != 1 :
                if (i+1)%j == 0 :
                    state = 1
        if state == 0 :
            factors.append(i+1)
            print(factors)
    state = 0

stop = time.time()
            

print(factors)
print(stop-start)


"""first iter


fact is, it wont find anything big but it doesnt stop anywhere
## 6857

"""

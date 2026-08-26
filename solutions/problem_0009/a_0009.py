for i in range(1 , 1001):
    for j in range(1 , 1001):
        if (1000-i-j)**2 == (i**2+j**2):
            print(i*j*(1000-i-j))

## 31875000
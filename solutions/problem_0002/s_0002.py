fibo = [1,2]
while fibo[-1] + fibo[-2] < 4e6:
    fibo.append(fibo[-1] + fibo[-2])
print(fibo[-1])

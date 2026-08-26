products = []
for i in range(100,1000):
    for j in range(100,1000):
        product =str(i*j)
        reverseproduct = product[::-1]
        if reverseproduct == product :
            products.append(int(product))

print(max(products))

## 906609

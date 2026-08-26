state = True
position = 21
counter = 0
while state :
    print(position)
    for i in range(1,21):
        if position%i == 0 :
            counter = counter + 1
            print(counter)
    if counter == 20:
        print(position)
        break
    else:
        counter = 0
    position = position + 1

## NO NEED FOR CODING 232792560

x = int(input("Imput integer number: "))
is_prime = True
div = 2

while div < x:
    if not x % div:
        is_prime = False
        break
    div += 1

if is_prime:
    print("Prime")
else:
    print("Not prime")
    
#for loop
x = int(input("Input integer number: "))

for div in range(2, x):
     if not x % div:
            print("Not prime")
            break
else:
     print("Prime")

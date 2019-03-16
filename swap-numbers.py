#get numbers
print("Choose two numbers:")
a = int(float(input()))
b = int(float(input()))

#store them in a tuple
tup = (a ,b)
print(tup)

#swap the numbers
(a, b) = (b, a)

#update tuple
tup = (a, b)
print(tup)
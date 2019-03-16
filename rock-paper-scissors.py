#get numbers
a = float(input())
b = float(input())
#store them in a tuple
tup = (a ,b)
print(tup)
#swap the numbers
(a, b) = (b, a)
print(tup)
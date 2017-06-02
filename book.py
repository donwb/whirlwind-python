mylist = [2, 3, 5, 7, 11]
print(mylist[-1])

# slicing
print(mylist[:3]) # first 3 elements
print(mylist[-3:]) # last 3 elements
print("Steps: ", mylist[::2]) # step - same as L[0:len(L):2] 
print("neg steps: ", mylist[::-1]) #basically reverse the list

#tuples are immutable lists
t = 1, 2, 3
print(t)

#tuple as a return value
x = 0.125
y = x.as_integer_ratio()
print(y) #tuple
#deconstruction
val1, val2 = x.as_integer_ratio()
print(val1, val2)
print(); print(); print();

### Dictionaries
numbers = {'one':1, 'two':2, 'three':3}
print(numbers['two'])
numbers['ninety'] = 90
print(numbers)

print(); print(); print();

midpoint = 5
lower = []; upper = []

# how youdo multiline
x = (1 + 2 +
3 + 4 + 5)
print(x)
y = 4.5
print(y.is_integer())


# split numbers into lower and upper
for i in range(10):
	if (i < midpoint):
		lower.append(i)
	else:
		upper.append(i)

print("Lower:", lower)
print("upper: ", upper)

s = "hello world"

print(len(s))
print(s.upper())
print(s.capitalize())

multi = 5 * s
print(multi)

l = [44, 2, 3, 4]
print(len(l))

l.append(11)
print(len(l))
print(l)

l.sort()
print(l)


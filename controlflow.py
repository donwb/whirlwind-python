#elif is a thing
x = -3
if x == 0:
	print(x, "is zero")
elif x > 0:
	print(x, "is positive")
elif x < 0:
	print(x, "is negative")
else:
	print(x, " is something else altogether")
	
for i in range(10):
	print(i, end=' ')
print()

alist = list(range(5, 10))
print(alist)
bytwo = list(range(0, 10, 2))
print(bytwo)

for n in range(20):
	if n % 2 == 0:
		continue
	print(n, end=' ')
print()

# loop-else
# the 'else' gets run if you never hit the break in the loop
x = 40
for i in range(20):
	if i == x:
		break
else:
	print("never found for 'x'")
	
print("done....")
print("again")



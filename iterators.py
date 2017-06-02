from itertools import count
# comment from Mac

#changes

I = iter([1, 2, 3, 4, 5])
print(next(I))
print(next(I))

# count is an endless iterator that will never stop counting
for i in count():
	if i >= 10:
		break
	print(i, end=', ')



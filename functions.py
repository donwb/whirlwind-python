#basic func
def fibonacci(N):
	L = []
	a, b = 0, 1
	while len(L) < N:
		a, b = b, a + b
		L.append(a)
	return L
	
#tuple return
def real_imag_conj(val):
	return val.real, val.imag, val.conjugate()

#default args
def fib_alt(N, a=0, b=1):
	L = []
	while len(L) < N:
		a, b = b, a + b
		L.append(a)
	return L

#args and kwargs (keyword args)
# * is expand as sequence and ** is expands as dict
def catch_all(*args, **kwargs):
	print("args=", args)
	print("kwargs=", kwargs)



catch_all(1, 2, 3, a=4, b=5)
catch_all('a', keyword=2)
# can also be used at the call site
inputs = (1, 2, 3)
keywords = {'pi': 3.14}
catch_all(*inputs, **keywords)


y = fib_alt(10, 3, 10)
print(y)

r, i, c = real_imag_conj(3 + 4j)
print(r, i, c)


x = fibonacci(10)
print(x)

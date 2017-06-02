def safe_devide(a, b):
    try:
        return a / b
    except ZeroDivisionError as err:
        print("Error is: ", err)
        print("Error type is ", type(err))
        return 1E100

x = safe_devide(1, 2)
print(x)

y = safe_devide(1, 0)
print(y)

#z = safe_devide(1, 'a')
#print(z)

def fib(N):
    if N < 0:
        raise ValueError("N must be nnn-neg")
    L = []
    a, b = 0, 1
    while len(L) < N:
        a, b = b, a + b
        L.append(a)
    return L

f = fib(10)
print(f)

# for illustration, there is lots of flow
def does_nothing():
    try:
        print("try something")
    except:
        print("bad things happened")
    else:
        print("happens only if success!")
    finally:
        print("happens no matter what!")

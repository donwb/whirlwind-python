primes = {2, 3, 5, 7}
odds = {1, 3, 5, 7, 9}
print("Primes: ", primes)
print("Odds:: ", odds)
print()

u = primes | odds #union
print(u)
i = primes & odds #intersection
print(i)

diff = primes - odds #difference
print(diff)




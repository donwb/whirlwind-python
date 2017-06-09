print("List")

# List - collection of values
L = [n ** 2 for n in range(12)]
for val in L:
	print(val, end=' ')
	
print("\n")	
print("Generator...")
# Generator - recipie for creating a list of values

G = (n ** 2 for n in range(12))
#generator created here, not up there...
for val in G:
	print(val, end=' ')
	
# Generators can only be used once,
# but they can be stopped/started
GG = (n**2 for n in range(12))
for n in GG:
	print(n, end=' ')
	if n > 30: break

print("\ndoing something in between")

for n in GG:
	print(n, end=' ')



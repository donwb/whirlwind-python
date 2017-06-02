# basic syntax
add = lambda x, y: x + y
la = add(1, 2)
print(la)

#complex example
data = [{'first':'Guido', 'last':'Van Rossum', 'YOB':1974},
				 {'first':'Grace', 'last':'Hopper', 'YOB':1906},
				 {'first':'Alan', 'last':'Turing', 'YOB':1912}]

# defines a func assigned to 'key', pass first name, return item
slist = sorted(data, key=lambda item:item['first'])
print(slist)

yoblist = sorted(data, key=lambda item:item['YOB'])
print(yoblist)

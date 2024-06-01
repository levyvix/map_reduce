from multiprocessing import Pool


def increase(x):
    return x + 1


with Pool() as p:
    a = p.map(increase, range(100))
    
    
with Pool() as p:
    b = p.imap(increase, range(100))
    
with Pool() as p:
	c = p.imap_unordered(increase, range(100))
 

print(a)
print(b)
print(c)
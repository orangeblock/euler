import itertools

def divisors(num):
	divisors = set()
	for i in xrange(1, int(num**0.5)+1):
		if num % i == 0:
			divisors.add(i)
			divisors.add(num/i)			
	return divisors

for num in itertools.count(1):
	tri = sum(xrange(num+1))
	if len(divisors(tri)) > 500:
		print tri
		break

n = 600851475143
factors = []
for i in xrange(2, int(n**0.5)+1):
    while n % i == 0:
        factors.append(i)
        n //= i
print max(factors)
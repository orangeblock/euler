def sieve(limit):
    if limit < 2: return []
    l = [2] + range(3, limit+1, 2) # use 2 and only odd numbers
    for i, num in enumerate(l):
        if num and i > 0:
            # remove all multiples of i which for odd numbers are:
            # 2i(i+1), 2i(i+1) + 2i+1, 2i(i+1) + 4i+2...
            for j in range(2*i*(i+1), len(l), 2*i+1):
                l[j] = False
    return [x for x in l if x]

if __name__ == '__main__':    
    print sum(sieve(2000000))
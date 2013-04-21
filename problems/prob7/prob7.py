# http://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test
def is_prime(num, repeat=5):
    if num == 2 or num == 3: return True
    if num <= 1 or num % 2 == 0: return False        

    s, d = 0, num-1
    while d % 2 == 0:
        s, d = s+1, d//2

    from random import randint
    for _ in xrange(repeat):
        x = pow(randint(2, num-2), d, num)
        
        if x == 1 or x == num-1: continue

        for _ in xrange(s):
            x = pow(x, 2, num)
            if x == 1: return False
            if x == num-1: break
        if x != num-1: return False

    return True

if __name__ == '__main__':
    n, pr = 2, 3
    while n < 10001:
        pr += 2
        if is_prime(pr):
            n += 1    
    print pr
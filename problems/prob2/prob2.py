def fib(limit):
    prev, curr = 0, 1
    while curr < limit:
        yield curr
        prev, curr = curr, curr+prev

print sum([x for x in fib(4000000) if x % 2 == 0])
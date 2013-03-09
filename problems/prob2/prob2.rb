def fib(limit)
    prev, curr = 0, 1
    while curr < limit do
        yield curr
        prev, curr = curr, curr+prev
    end
end

nums = []
fib(4_000_000) { |n| nums << n if n.even? }
puts nums.inject { |sum, n| sum + n }
n = 600851475143
factors = []
2.upto(n**0.5) do |i|
    until n % i != 0 do
        factors << i
        n /= i
    end
end
puts factors.max
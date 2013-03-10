digits = IO.read('digits.txt').split('').map { |d| d.to_i }

products = []
digits.each_index { |i| products << digits[i, 5].inject(:*) if i <= digits.size-5 }

puts products.max
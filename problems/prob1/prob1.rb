total = 0
1.upto(999) { |n| total += n if n%3 == 0 or n%5 == 0 }
puts total
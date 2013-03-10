with open('digits.txt') as f:
    digits = map(int, list(f.read()))
print max( [reduce(lambda x, y: x*y, digits[i:i+5]) for i in range(len(digits)-5)] )
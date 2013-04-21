for c in range(1, 1000):
    for b in range(1, c):
        a = int((c**2 - b**2)**.5)
        if a + b + c == 1000 and a**2 + b**2 == c**2:
            print a*b*c
            break
tri = list(map(int, row.split()) for row in open('triangle.txt'))[::-1]

for i in range(1, len(tri)):
    tri[i] = [x + max(tri[i-1][j], tri[i-1][j+1]) for j, x in enumerate(tri[i])]

print tri[-1][0]

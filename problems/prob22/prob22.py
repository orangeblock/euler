alphabet = '_ABCDEFGHIJKLMNOPQRSTUVWXYZ'
names = sorted(open('names.txt').read().split(','))
names = [0] + [name.strip('"') for name in names]

def score(name):
    return names.index(name) * sum(map(alphabet.index, name))

print sum(map(score, names[1:]))
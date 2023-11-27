d = {'k': 2}
d2 = {'k': 1}

l = [d, d2]
l = iter(l)

print(next(l)['k'])

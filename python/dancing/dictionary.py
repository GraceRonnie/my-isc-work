band = ['Mel', 'Geri', 'Victoria', 'Mel', 'Emma']
counts = {}

for name in band:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] += 1

for name in counts:
    print name, counts[name]

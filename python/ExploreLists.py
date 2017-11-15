forward = []
backward = []
values = ["a", "b", "c"]
for item in values:
    forward.append(item)
    backward.insert(0, item)

print "forward is:", forward
print "backward is:", backward

forward.reverse()
print forward ==backward
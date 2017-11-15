mylist = [23, "hi", 2.4E-10]
(first, middle, last) = mylist
print first
print last
(first, middle, last) = (middle, last, first)
print first, middle, last

#note it doesn't matter again what the words are it only understands in context, e.g. last replced with cat

mylist = [23, "hi", 2.4E-10]
(first, middle, cat) = mylist
print first
print cat
(first, middle, cat) = (middle, cat, first)
print first, middle, last
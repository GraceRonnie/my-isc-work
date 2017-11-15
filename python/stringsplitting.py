s = 'I love to write Python'
split_s = s.split() #unless told otherwise it assumes split by spaces, if want to split commans then need x.split(',')
print split_s
for word in split_s:
    if word.find("i") > -1:   #if not there gives -1, here we're saying if it's more than -1 then it's true it's there
        print "I found 'i' in: '{0}'".format(word) #outputs gives i in 'write'
if 'i' in word:
    print "I found 'i' in '{0}'".format(word)


with open("weather.csv") as reader:
    line = reader.readline() #readline() means read all the  first line
    while line:
        print line
        line = reader.readline()

print "it's over"

#this reads the first line and then loops to read each sequential line until there is an empty string i.e. no more lines and then says it's over
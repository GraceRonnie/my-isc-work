with open("weather.csv", "r") as reader: #translates as open the file in read mode and call this 'variable' reader
    data = reader.read() #read the variable "reader" and call this data
print data

#this reads the file to me in shell
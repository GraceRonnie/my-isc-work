with open("weather.csv") as reader:
    header = reader.readline()
    rain = []
    for line in reader.readlines():
        r = line.strip() .split(",") [-1] #strip down each line into chunks as separated by commas and show final chunk
        r = float(r)  #float means give decimal places if not then would give 4 not 4.4500 etc
        rain.append(r) #add the value of r to the empty list named rain above

print rain
with open("myrain.txt", "w") as writer:
    for r in rain: 
        writer.write(str(r) + "\n") #here we're also writing these values of r into the file myrain.txt
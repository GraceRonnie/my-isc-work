def convert_time(tm):
    tm  = datetime.strptime(tm, "%Y-%m-%dT%H:%M:%S.%f")
    return tm

def convert_temp(temp)
    value = temp.strip("+").strip("C").lstrip("0")
    return float(value) + 273.15

infile = 'example_data/sample-serial-temperature-2h.tsv'
outfile = 'sensor-data.nc'
from csv import reader

times = []
temps = []

with open(infline, 'rb') as tsvfile:
    tsvreader = reader(tsvfile, delimiter='\t')
    for row in tsvreader:
        times.append(convert_time(row[0]))
        temps.append(convert_temp(row[1]))
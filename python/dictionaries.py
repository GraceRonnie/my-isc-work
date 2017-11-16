if {}: print "hi"

d = {"maggie": "uk", "ronnie": "usa"}
d.items() #items returns [('maggie', 'uk'), ('ronnie', 'usa')] i.e. the contents of the dictionary in their paired tuples
d.keys() #keys returns ['maggie', 'ronnie']
d.values() #values returns ['uk', 'usa']

d.get("maggie", "nowhere") #returns uk
d.get("ringo", "nowhere") #returns nowhere

res = d.setdefault("mikhail", "ussr")
print res, d["mikhail"] #returns ussr ussr

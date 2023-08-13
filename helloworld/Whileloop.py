data='From stephen.marquard@uct.ac.za mon may 17 12:14:16 2021'
atpos=data.find('@')
print(atpos)
sspos=data.find(' ',atpos)
print(sspos)
host=data[atpos+1:sspos]
print(host)


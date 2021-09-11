s=input()
for a,b in zip("OLZEASGTBQolzeasgtbq","0123456789"*2):s=s.replace(a,b)
print(s)

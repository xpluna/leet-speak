l={'O':'0','L':'1','Z':'2','E':'3','A':'4','S':'5','G':'6','T':'7','B':'8','Q':'9'}
for p in input():print(p if p.upper()not in l.keys()else l[p.upper()],end="")

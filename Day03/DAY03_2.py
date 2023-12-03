g = open("DAY03.txt").read().splitlines()
t = 0

for r1, r2 in enumerate(g):
    for c1, c2 in enumerate(r2):
        if c2 != "*":
            continue
            
        c3 = set()
        
        for cr in [r1 -1, r1, r1 + 1]:
            for cc in [c1 -1, c1, c1 + 1]:
                if cr < 0 or cr >= len(g) or cc < 0 or cc >= len(g[cr]) or not g[cr][cc].isdigit():
                    continue
                while cc > 0 and g[cr][cc - 1].isdigit():
                    cc -= 1
                c3.add((cr, cc))
        
        if len(c3) != 2:
            continue
            
        ns = []
        
        for cr, cc in c3:
            s = ""
            while cc < len(g[cr]) and g[cr][cc].isdigit():
                s += g[cr][cc]
                cc += 1
            ns.append(int(s))
            
        t += ns[0] * ns[1]
    
    print(t)     
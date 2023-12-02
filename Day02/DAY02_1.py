import re
p1 = r'\s(\d+)\s(blue|green|red)'
gnum = ['0', '0']
total = 0
for record in open("DAY02.txt"):
    games = record.split("\n")
    for game in games:
        for set in game.split(":"):
            for rgb in set.split(" ;"):
                if len(rgb) <= 10:
                    if len(rgb) > 0:
                        gnum = rgb.split(" ")
                        print("A:", gnum[1])
                else:
                    for i in rgb.split(";"):
                        for j in i.split(","):
                            m = re.findall(p1, j)
                            if (m[0][1] == "blue"):
                                if (int(m[0][0]) >14):
                                    print("Invalid:", "B:", m[0][0])
                                    gnum[1] = 0
                                else:
                                    print("B:", m[0][0])
                            if (m[0][1] == "green"):
                                if (int(m[0][0]) > 13):
                                    print("Invalid:", "G:", m[0][0])
                                    gnum[1] = 0
                                else:
                                    print("G:", m[0][0])
                            if (m[0][1] == "red"):
                                if (int(m[0][0]) > 12):
                                    print("Invalid:", "R:", m[0][0])
                                    gnum[1] = 0
                                else:
                                    print("R:", m[0][0])
   
    total += int(gnum[1])
            
print (total)
import re
p = r'((\s(\d+)\s)(blue|red|green){1,3})'
gnum = ['A:', 0, 0, 0, 0]
total = 0
for record in open("DAY02.txt"):
    games = record.split("\n")
    for game in games:
        for set in game.split(":"):
            for rgb in set.split(" ;"):
                if len(rgb) <= 10:
                    if len(rgb) > 0:
                        temp = rgb.split(" ")
                        gnum[1] = int(temp[1])
                        print(gnum[0], gnum[1])
                        print (gnum[2])
                        print (gnum[3])
                        print (gnum[4])
                        gnum[2] = 0
                        gnum[3] = 0
                        gnum[4] = 0
                else:
                    for colour in rgb.split(";"):
                        m = re.findall(p, colour)

                        print ("m[0][2]", m[0][2])
                        print ("m[0][3]", m[0][3])
                        if (m[0][3] == "blue"):
                            if (gnum[2] < int(m[0][2])):
                                gnum[2] = int(m[0][2])
                        if (m[0][3] == "green"):
                            if (gnum[3] < int(m[0][2])):
                                gnum[3] = int(m[0][2])
                        if (m[0][3] == "red"):
                            if (gnum[4] < int(m[0][2])):
                                gnum[4] = int(m[0][2])
                        try:
                            print ("m[1][2]",m[1][2])
                            print ("m[1][3]",m[1][3])
                            if (m[1][3] == "blue"):
                                if (gnum[2] < int(m[1][2])):
                                    gnum[2] = int(m[1][2])
                            if (m[1][3] == "green"):
                                if (gnum[3] < int(m[1][2])):
                                    gnum[3] = int(m[1][2])
                            if (m[1][3] == "red"):
                                if (gnum[4] < int(m[1][2])):
                                    gnum[4] = int(m[1][2])
                        except:
                            pass
                        try:
                            print ("m[2][2]", m[2][2])
                            print ("m[2][3]", m[2][3])
                            if (m[2][3] == "blue"):
                                if (gnum[2] < int(m[2][2])):
                                    gnum[2] = int(m[2][2])
                            if (m[2][3] == "green"):
                                if (gnum[3] < int(m[2][2])):
                                    gnum[3] = int(m[2][2])
                            if (m[2][3] == "red"):
                                if (gnum[4] < int(m[2][2])):
                                    gnum[4] = int(m[2][2])
                        except:
                            pass
    print(gnum[2], " ", gnum[3], " ", gnum[4])
    total += gnum[2] * gnum[3] * gnum[4]
    print (total)   
print (total)
predelim = input("Please input x1, y1, x2, and y2 seperated by spaces, ie: 3 4 7 -8: ")
delim = [int(x) for x in predelim.split()]
m = (delim[3] - delim[1]) / (delim[2] - delim[0])
print(m)
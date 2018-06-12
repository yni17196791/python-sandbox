f = open("printed.txt", "r")
areas = f.readlines()
areas[0] = areas[0].strip("\n")

print(areas[0])
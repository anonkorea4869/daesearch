with open("regex.txt", "r") as file:
    lines = [line.rstrip() for line in file]

for line in lines :
    print(line.split("/"))
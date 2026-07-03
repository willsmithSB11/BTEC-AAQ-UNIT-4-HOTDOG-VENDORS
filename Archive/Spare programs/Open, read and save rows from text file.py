hotdogVendors = []

file = open("Hotdogs.txt", "r")

for line in file:
    row = line.strip().split(",")
    hotdogVendors.append(row)
    print(row)
file.close()

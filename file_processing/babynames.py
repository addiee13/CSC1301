try:
    with open("name_data.txt", "r") as infile:
        for line in infile:
            data = line.rstrip().split()
            boys = data[0::2]
            girls = data[3:]
            girls.insert(0, data[0])
            print(boys, girls)
        
except FileNotFoundError:
    print("File not found!")
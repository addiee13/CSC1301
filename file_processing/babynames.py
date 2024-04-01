def get_popular_boy_names(infile):
    boys = []
    for line in infile:
        data = line.rstrip().split()
        boys.append(data[0:3])
        for boy in boys:
            boy[-1] = str(boy[-1]).rstrip("%")
            boy[-1] = float(boy[-1])
    return boys

def get_popular_girl_names(infile):
    infile.seek(0) #sets pointer to beginning because boys function sets the pointer to end
    girls = []
    for line in infile:
        data = line.rstrip().split()
        girls.append(data[3:])
        for girl in girls:
           girl[-1] = float(str(girl[-1]).rstrip("%"))  
    return girls


try:
    with open("name_data.txt", "r") as infile:       
        print(get_popular_girl_names(infile))    
except FileNotFoundError:
    print("File not found!")
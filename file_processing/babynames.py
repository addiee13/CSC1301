def get_popular_boy_names(infile):
    '''@return A list with boy name, percentage '''
    boys = []
    for line in infile:
        data = line.rstrip().split()
        boys.append(data[1:3])
        for boy in boys:
            boy[-1] = str(boy[-1]).rstrip("%")
            boy[-1] = float(boy[-1])
    return boys

def get_popular_girl_names(infile):
    '''@return A list with girl name, percentage '''
    infile.seek(0) #sets pointer to beginning because boys function sets the pointer to end
    girls = []
    for line in infile:
        data = line.rstrip().split()
        girls.append(data[3:])
        for girl in girls:
           girl[-1] = float(str(girl[-1]).rstrip("%"))  
    return girls

def get_top_50_boy(infile):
    boys = get_popular_boy_names(infile)
    percent = 0
    for boy in boys:
        percent += (boy[-1])
    boys_50 = []
    count = 0 
    for boy in boys:
        if count <= percent/2:
            boys_50.append(boy[0])
            count += boy[1]
    return boys_50

def get_top_50_girl(infile):
    girls = get_popular_girl_names(infile)
    percent = 0
    for girl in girls:
        percent += (girl[-1])
    girls_50 = []
    count = 0 
    for girl in girls:
        if count <= percent/2:
            girls_50.append(girl[0])
            count += girl[1]
    return girls_50

try:
    with open("name_data.txt", "r") as infile:   
        # print(f"The top 50% of 100 most common names are:   {get_top_50_boy(infile)}")    
        print(f"The top 50% of 100 most common girl names are:   {get_top_50_girl(infile)}") 
except FileNotFoundError:
    print("File not found!")
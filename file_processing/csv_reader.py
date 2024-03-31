from csv import reader
with open("movies.csv", "r") as infile:
    csv_reader = reader(infile)
    next(csv_reader)
    highest_amt = 0
    lowest_amt = 999999
    for row in csv_reader:
        row[6] = row[6].strip("$")
        if float(row[6]) >= highest_amt:
            highest_amt = float(row[6])
            high_gross = row[0]
        if float(row[6]) <= lowest_amt:
            lowest_amt = float(row[6])
            low_gross = row[0]  
    print(f"The highest grossing film is {high_gross} and it collected {highest_amt} million dollars.")
    print(f"The lowest grossing film is {low_gross} and it collected {lowest_amt} million dollars.")
names = ["riyan", "Rohaan", "Ayuhsman", "Adam", "Nousheen", "Sneh", "Harini", "Krisha"]
names_n = []
for name in names:
    if name[-1] == 'n':
        names_n.append(name)
for name in names_n:
    print(name.title())

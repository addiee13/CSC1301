total = 0
count = 0
with open("numbers.txt", 'r') as infile:
    with open("solution.txt", "w") as outfile:
        for line in infile:
            total += float(line)
            print(f'{" "*10}{float(line):.2f}', file=outfile)
            count += 1
        print(f'{" "*7}{"-"*8}', file=outfile)
        print(f"Total:{' '*3}{total:.2f}", file=outfile)
        print(f"Count:{' '*5}{count:.2f}", file=outfile)
        print(f"Average:{' '*2}{total/count:.2f}", file=outfile)
        
        
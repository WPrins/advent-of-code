import csv

result = 0
with open("day2Input.txt") as input:
    data = csv.reader(input, delimiter='\t')
    for line in data:
        smallest = line[0]
        largest = line[0]
        for item1 in line:
            for item2 in line:
                if not(item2 is item1):
                    fraction = float(item1)/float(item2)
                    if fraction == round(fraction):
                        result += int(fraction)
print(result)
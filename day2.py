import csv

result = 0
with open("day2Input.txt") as input:
    data = csv.reader(input, delimiter='\t')
    for line in data:
        smallest = line[0]
        largest = line[0]
        for item in line:
            if int(item) > int(largest):
                largest = item
            if int(item) < int(smallest):
                smallest = item
        result += (int(largest) - int(smallest))
print(result)
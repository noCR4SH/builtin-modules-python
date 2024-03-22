import csv

# Data example
data = [
    ["Name", "Age", "City"],
    ["Alice", 25, "Boston"],
    ["Bob", 30, "Chicago"]
]
# Writing into csv file
with open('example.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

# Reading from csv file
with open('example.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

# Using DictWriter to write to a csv
fieldnames = ["Name", "Age", "City"]
person1 = {
    'Name': 'Alice',
    'Age': 25,
    "City": "Boston"
}
person2 = {
    'Name': 'Bob',
    'Age': 30,
    "City": "Chicago"
}
with open('example_dict.csv', 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow(person1)
    writer.writerow(person2)

# Reading using DictReader
with open('example_dict.csv', 'r') as file:
    reader = csv.DictReader(file)
    print(reader)
    for row in reader:
        print(row)
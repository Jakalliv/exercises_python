import csv

# Open the CSV file in 'read' mode with UTF-8 encoding
with open('example.csv', 'r', encoding='utf8') as file:
  # Create a CSV reader object
  csv_reader = csv.reader(file)

  for row in csv_reader:
    print(row)
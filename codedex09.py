import csv
x = []
y = []
# Open the CSV file in 'read' mode with UTF-8 encoding
with open('Bestseller - Sheet1.csv', 'r', encoding='utf8') as file:
  # Create a CSV reader object
  csv_reader = csv.reader(file)

  for row in csv_reader:
    x.append(row)
    try:
      y.append(float(row[4]))
    except ValueError:
      pass

with open("bestseller_info.csv ", "w", newline= "", encoding='utf-8') as file:
  writer = csv.writer(file)
  writer.writerow(x[y.index(max(y))+1])
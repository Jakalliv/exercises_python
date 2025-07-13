import csv 

data = [
  ['Item', 'Quantity'],
  ['Blender', 2],
  ['Posters', 30],
  ['Shoes', 2]
]
try:
    with open('filename.txt', 'r') as file:
        reader = file.read()
        for row in reader:
            print(row)
except FileNotFoundError as e:
    print(e)
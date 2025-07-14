import csv 

data = [
  ['Item', 'Quantity'],
  ['Blender', 2],
  ['Posters', 30],
  ['Shoes', 2]
]
try:
    with open('Packing List.csv', 'r', encoding = "utf8") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)
except FileNotFoundError as e:
    print(f"Error: {e}. The Packing list file will be added.")
    with open ("Packing List.csv", "w", newline="", encoding = "utf8") as file:
      writer = csv.writer(file)
      writer.writerows(data)
      print("Packing list created successfully.")
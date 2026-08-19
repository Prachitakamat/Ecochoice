import csv

with open("cleaning.csv", newline="", encoding="utf-8") as f:
    reader = csv.reader(f)

    for row_num, row in enumerate(reader, 1):
        if len(row) != 8:
            print("PROBLEM:", row_num, "has", len(row), "columns")
            print(row)
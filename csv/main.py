import csv

# writing to a CSV file
file = open("example.csv", "w", newline="")
try:
    writer = csv.writer(file)
    writer.writerow(["Danrlei", "41999999999", "4133333333"])
    writer.writerow(["Maria", "41999999999", "4133333333"])
    writer.writerow(["Angela", "41999999999", "4133333333"])
finally:
    file.close()

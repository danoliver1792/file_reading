import csv

# inserting multiple phones into a CSV
phones = [["Danrlei", "41999999999", "4133333333"],
          ["Maria", "41999999999", "4133333333"],
          ["Angela", "41999999999", "4133333333"]]

with open("example2.csv", "w", newline="") as arq:
    writer = csv.writer(arq)
    writer.writerows(phones)

from urllib.request import urlretrieve
import csv

# opening CSV through a link
link = input("Inform the link: ")
delimiter = input("Inform the delimiter: ")
urlretrieve(link, "file_download.csv")

with open("file_download.csv", "r") as file_csv:
    reader = csv.reader(file_csv, delimiter=delimiter)
    for row in reader:
        print(row)

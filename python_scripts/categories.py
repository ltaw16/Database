import xml.etree.ElementTree as ET
import csv

tree = ET.parse("../xml_files/Category_Code.xml")
root = tree.getroot()

# open a file for writing

Main_data = open('../parsed_files/categories.csv', 'w')

# create the csv writer object

csvwriter = csv.writer(Main_data)
for category in root:

    load = []
    catcode = category.find('catcode').text
    catexplain = category.find('catexplain').text
    load.append(catcode)
    load.append(catexplain)
    print(load)
    csvwriter.writerow(load)


Main_data.close()

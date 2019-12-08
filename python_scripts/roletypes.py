import xml.etree.ElementTree as ET
import csv

tree = ET.parse("../xml_files/role_type.xml")
root = tree.getroot()

# open a file for writing

Main_data = open('../parsed_files/roletypes.csv', 'w')

# create the csv writer object

csvwriter = csv.writer(Main_data)
for category in root:

    load = []
    rlcode = category.find('rlcode').text
    rlexplain = category.find('rlexplain').text
    load.append(rlcode)
    load.append(rlexplain)
    print(load)
    csvwriter.writerow(load)


Main_data.close()

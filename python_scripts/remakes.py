import xml.etree.ElementTree as ET
import csv

tree = ET.parse("../xml_files/remakes05.xml")
root = tree.getroot()

# open a file for writing

Main_data = open('../parsed_files/remakes.csv', 'w')

# create the csv writer object

csvwriter = csv.writer(Main_data)
for remake in root:
    main = []
    load = []
    main.append(remake.find('rid'))
    main.append(remake.find('rtitle'))
    main.append(remake.find('ry'))
    main.append(remake.find('frac'))
    main.append(remake.find('sid'))
    for item in main:
        if item is None:
            load.append(None)
        else:
            load.append(item.text)


    print(load)
    csvwriter.writerow(load)

Main_data.close()

import xml.etree.ElementTree as ET
import csv

tree = ET.parse("../xml_files/casts124.xml")
root = tree.getroot()

# open a file for writing

Casts_data = open('../parsed_files/casts.csv', 'w')

# create the csv writer object

csvwriter = csv.writer(Casts_data)
casts_head = []

for member in root.findall('.//filmc'):
    for person in member.findall('m'):
        attribute_list = ["f", "t", "a", "p", "r", "n", "awards"]
        row = []
        for attribute in attribute_list:
            if attribute == "awards":
                awardStr = ""
                awards = person.findall('.//award')
                for award in awards:
                    awardStr += award.text
                row.append(awardStr)
            elif person.find(attribute) is None:
                row.append(None)
            else:
                row.append(person.find(attribute).text)

        print('ROW: ', row)
        csvwriter.writerow(row)

Casts_data.close()

import xml.etree.ElementTree as ET
import csv

tree = ET.parse("../xml_files/people55.xml")
root = tree.getroot()

# open a file for writing

People_data = open('../parsed_files/people.csv', 'w')

# create the csv writer object

csvwriter = csv.writer(People_data)
people_head = []

for member in root.findall('person'):
    attribute_list = ["pname", "did", "dob", "dod", "yearstart", "yearend", "familynm", "background", "pcode", "yeardirstart", "givennm"]
    person = []
    for attribute in attribute_list:
        if attribute == "pcode":
            pcodeString = ""
            pcodes = member.find("pcodes")
            for pcode in pcodes:
                pcodeString += pcode.text
            person.append(pcodeString)
        elif member.find(attribute) is None:
            person.append(None)
        else:
            person.append(member.find(attribute).text)

    csvwriter.writerow(person)

People_data.close()

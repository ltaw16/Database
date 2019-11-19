import xml.etree.ElementTree as ET
import csv

tree = ET.parse("../xml_files/actors63.xml")
root = tree.getroot()

# open a file for writing

Actor_data = open('../parsed_files/actors.csv', 'w')

# create the csv writer object

csvwriter = csv.writer(Actor_data)
actor_head = []

for member in root.findall('actor'):
    attribute_list = ["stagename", "familyname", "roletype", "picref", "dob", "dowstart", "dod", "dowend"]
    actor = []
    for attribute in attribute_list:
        if member.find(attribute) is None:
            actor.append(None)
        else:
            actor.append(member.find(attribute).text)
        print(attribute)
    csvwriter.writerow(actor)

    # stage_name = member.find('stagename').text
    # actor.append(stage_name)
    # # real_first_name = member.find('firstname').text
    # family_name = member.find('familyname').text
    # # real_name = real_first_name + " " + family_name
    # # actor.append(real_name)
    # actor.append(family_name)
    # # TODO: figure out how to handle background
    # actor.append(None)
    # type_of_role = member.find('roletype').text
    # actor.append(type_of_role)
    # # images = member.find('picref').text
    # images = None
    # actor.append(images)
    # dob = member.find('dob').text
    # actor.append(dob)
    # dow_start = member.find('dowstart').text
    # actor.append(dow_start)
    # dod = member.find('dod').text
    # actor.append(dod)
    # dow_end = member.find('dowend').text
    # actor.append(dow_end)
Actor_data.close()

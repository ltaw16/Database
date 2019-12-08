import xml.etree.ElementTree as ET
import csv

tree = ET.parse("../xml_files/mains243.xml")
root = tree.getroot()

# open a file for writing

Main_data = open('../parsed_files/movie_awards.csv', 'w')

# create the csv writer object

csvwriter = csv.writer(Main_data)
attribute_list = ["fid", "t", "year"]
print(root.findall('directorfilms'))
for attr in root.findall('directorfilms'):
    films = attr.find('films')
    for film in films:
        if film.tag == "film":
            awards = film.find("awards")
            if awards is not None:
                for award in awards:
                    main = []
                    awards_list = [award.find("awtype"), award.find("awattr")]
                    for attribute in attribute_list:
                        if film.find(attribute) is None:
                            main.append(None)
                        else:
                            main.append(film.find(attribute).text)
                    for x in awards_list:
                        if x is not None:
                            main.append(x.text)
                    print(main)
                    csvwriter.writerow(main)

#
# for member in root.findall('film'):
#     print(member)
#     # table attributes: title, year of release, topic,  diretor, history, type, producer, award name, original title, original year, fraction_sig
#     attribute_list = ["t", "year", "fid"]
#     main = []
#     for attribute in attribute_list:
#         if member.find(attribute) is None:
#             main.append(None)
#         else:
#             main.append(member.find(attribute).text)
#         print(main)
#

Main_data.close()

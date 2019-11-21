import xml.etree.ElementTree as ET
import csv

tree = ET.parse("../xml_files/mains243.xml")
root = tree.getroot()

# open a file for writing

Main_data = open('../parsed_files/movie_studio.csv', 'w')

# create the csv writer object

csvwriter = csv.writer(Main_data)
for attr in root.findall('directorfilms'):
    films = attr.find('films')
    for film in films:
        if film.tag == 'film':
            film_id = film.find('fid')
            title = film.find('t')
            studios = film.find('studios')
            if studios is not None:
                for studio in studios:
                    main = []
                    load = []
                    if studio.tag == 'studio':
                        main.append(film_id)
                        main.append(title)
                        main.append(studio)
                        for item in main:
                            if item is None:
                                load.append(None)
                            else:
                                load.append(item.text)

                    print(load)
                    csvwriter.writerow(load)

Main_data.close()

from bs4 import BeautifulSoup
import lxml.html.soupparser
import csv

html = open("../xml_files/studios.htm").read()
soup = BeautifulSoup(html, 'lxml')

# finds only one "table"
# there are 3 in the source html
table = soup.find("table")

Studios_data = open('../parsed_files/studios.csv', 'w')
writer = csv.writer(Studios_data)

for row in table.findAll('tr'):
    columns = row.findAll('td')
    output_row = []
    for column in columns:
        if column is None:
            output_row.append(None)
        else:
            output_row.append(column.get_text(strip=True))

    print(output_row)

    writer.writerow(output_row)

Studios_data.close()

# needed for connection
# tutorial website: https://pynative.com/python-postgresql-tutorial/
# psycopg doc: http://initd.org/psycopg/docs/cursor.html#fetch

import psycopg2 as psycopg2
import csv
import re


def main():
    """load people"""
    load_people()


def load_people():
    regex = "\d{4}"
    try:
        conn = psycopg2.connect(host="10.90.10.41",
                                database="yikes",
                                user="ltaw16",
                                password="oracle")
        cursor = conn.cursor()

        with open('parsed_files/people.csv') as csv_file:

            csv_data = csv.reader(csv_file)
            dateIndicies = [2, 3, 4, 5, 9]
            for row in csv_data:
                for index in dateIndicies:
                    if row[index] == "" or row[index] == " " or row[index] == "\\Un" or row[index] == "*":
                        row[index] = None
                    elif row[index][-1:] == '+' or row[index][-1:] == '-' or row[index][-1:] == '?' or row[index][-1:] == '`':
                        row[index] = row[index][:-1]
                    elif len(row[index]) == 9:
                        row[index] = row[index][:-5]
                    elif len(row[index]) == 5 and row[index][-1:] == 'x':
                        row[index] = row[index][:-1]
                    elif not re.match(regex, row[index]):
                        row[index] = None

                print(row)
                cursor.execute('INSERT INTO person VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)', row)

        # just testing stuff
        # name, id, doc, dod, dow_start, dow_end, real_name, background, type, dow_dir_start, first_name
        # cursor.execute("insert into actor (stage_name, real_name, background, type_of_role, images, dob, dow_start, dod, dow_end) values ('Willie Aames', null, null, 'unknown', null, 1960, null, 1984, null);")
        # cursor.execute("insert into person values('Aaron', 'PAa', NULL, NULL, NULL, NULL, 'Aaron', '\Am', 'D', 1979, 'Paul');")

        conn.commit()
        count = cursor.rowcount
        print(count, "record inserted successfully into person table")
        # for record in cursor:
        #     print(record)

    except (Exception, psycopg2.Error) as error:
        print("error while connecting to postgresql", error)
    finally:
        if(conn):
            cursor.close()
            conn.close()
main()
# needed for connection
# tutorial website: https://pynative.com/python-postgresql-tutorial/
# psycopg doc: http://initd.org/psycopg/docs/cursor.html#fetch

import psycopg2 as psycopg2
import csv
import re


def main():
    print("hello world")

    # UNCOMMENT THIS TO ACTUALLY RUN
    # load_actors()


def load_actors():
    regex = "\d{4}"
    try:
        conn = psycopg2.connect(host="10.90.10.41",
                                database="yikes",
                                user="ltaw16",
                                password="oracle")
        cursor = conn.cursor()

        with open('parsed_files/actors.csv') as csv_file:

            csv_data = csv.reader(csv_file)
            for row in csv_data:
                print(row)
                print(len(row))
                for i in range(5, len(row)):
                    if row[i] == "" or row[i] == " " or row[i] == "n.a." or row[i] == "*" or row[i] == "dob":
                        row[i] = None
                    elif row[i][-1:] == '+' or row[i][-1:] == '-':
                        row[i] = row[i][:-1]
                    elif row[i][-1:] == 'x':
                        row[i] = row[i][:-1] + '0'
                    elif row[i][-2:] == "bb":
                        row[i] = row[i][:-2] + '00'
                    elif row[i][0:] == "[1]":
                        row[i] = row[i][:3]
                    elif not re.match(regex, row[i]):
                        row[i] = None

                cursor.execute('INSERT INTO actor VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)', row)
        # just testing stuff
        # stage name, real name, background, type of tole, images, dob, dowstart, dod, dow end,
        # cursor.execute("insert into actor (stage_name, real_name, background, type_of_role, images, dob, dow_start, dod, dow_end) values ('Willie Aames', null, null, 'unknown', null, 1960, null, 1984, null);")
        # cursor.execute("insert into actor values('Willie Aames', NULL, NULL, 'unknown', NULL, 1960, NULL, 1984, NULL);")

        conn.commit()
        count = cursor.rowcount
        print(count, "record inserted successfully into actor table")
        # for record in cursor:
        #     print(record)

    except (Exception, psycopg2.Error) as error:
        print("error while connecting to postgresql", error)
    finally:
        if(conn):
            cursor.close()
            conn.close()
main()
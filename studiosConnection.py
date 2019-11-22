# needed for connection
# tutorial website: https://pynative.com/python-postgresql-tutorial/
# psycopg doc: http://initd.org/psycopg/docs/cursor.html#fetch

import psycopg2 as psycopg2
import csv
import re


def main():
    """load people"""
    load_studios()


def load_studios():
    regex = "\d{4}"
    try:
        conn = psycopg2.connect(host="10.90.10.41",
                                database="yikes",
                                user="ltaw16",
                                password="oracle")
        cursor = conn.cursor()

        with open('parsed_files/studios.csv') as csv_file:
            errors = []
            csv_data = csv.reader(csv_file)
            dateIndicies = [4, 5]
            for row in csv_data:
                for index in dateIndicies:
                    if row[index] == "" or row[index] == " " or row[index] == "\\Un" or row[index] == "*":
                        row[index] = None
                    elif row[index][-1:] == '+' or row[index][-1:] == '-' or row[index][-1:] == '?' or row[index][-1:] == '`':
                        row[index] = row[index][:-1]
                    # elif len(row[index]) == 9:
                    #     row[index] = row[index][:-5]
                    # elif len(row[index]) == 5 and row[index][-1:] == 'x':
                    #     row[index] = row[index][:-1]
                    elif not re.match(regex, row[index]):
                        row[index] = None
                try:
                    print(row)
                    cursor.execute('INSERT INTO studio VALUES(%s,%s,%s,%s,%s,%s,%s,%s)', row)
                    conn.commit()
                except(Exception, psycopg2.Error) as error:
                    errors.append(row)
                    print("Error: ", error)
                    continue

        count = cursor.rowcount
        print(count, "record inserted successfully into studio table")
        # for record in cursor:
        #     print(record)

    except (Exception, psycopg2.Error) as error:
        print("error while connecting to postgresql", error)
    finally:
        if(conn):
            cursor.close()
            conn.close()
main()
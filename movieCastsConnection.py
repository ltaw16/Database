# needed for connection
# tutorial website: https://pynative.com/python-postgresql-tutorial/
# psycopg doc: http://initd.org/psycopg/docs/cursor.html#fetch

import psycopg2 as psycopg2
import csv
import re


def main():
    """load casts"""
    load_casts()


def load_casts():
    regex = "\d{4}"
    try:
        conn = psycopg2.connect(host="10.90.10.41",
                                database="yikes",
                                user="ltaw16",
                                password="oracle")
        cursor = conn.cursor()

        with open('parsed_files/casts.csv') as csv_file:
            errors = []
            csv_data = csv.reader(csv_file)
            for row in csv_data:
                try:
                    print(row)
                    cursor.execute('begin')
                    cursor.execute('INSERT INTO movie_cast VALUES(%s,%s,%s,%s,%s,%s,%s)', row)
                    conn.commit()
                except(Exception, psycopg2.Error) as error:
                    errors.append(row)
                    cursor.execute('abort')
                    continue

        count = cursor.rowcount
        print(count, "record inserted successfully into casts table")
        # for record in cursor:
        #     print(record)

    except (Exception, psycopg2.Error) as error:
        print("error while connecting to postgresql", error)
    finally:
        if(conn):
            cursor.close()
            conn.close()
    print(errors)
main()
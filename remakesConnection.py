# needed for connection
# tutorial website: https://pynative.com/python-postgresql-tutorial/
# psycopg doc: http://initd.org/psycopg/docs/cursor.html#fetch

import psycopg2 as psycopg2
import csv
import re


def main():
    # print('to run this program, uncomment load_movie_titles below')
    #
    load_movie_remakes()


def load_movie_remakes():
    try:
        conn = psycopg2.connect(host="10.90.10.41",
                                database="yikes",
                                user="ltaw16",
                                password="oracle")
        cursor = conn.cursor()

        with open('parsed_files/remakes.csv') as csv_file:
            errors = []
            csv_data = csv.reader(csv_file)
            for row in csv_data:
                print(row)
                # cursor.execute('INSERT INTO movie_directors VALUES(%s,%s,%s,%s,%s)', row)
                try:
                    cursor.execute('begin')
                    cursor.execute(
                        'INSERT INTO remakes VALUES(%s,%s,%s,%s,%s)',
                        row)
                    conn.commit()
                except(Exception, psycopg2.Error) as error:
                    errors.append(row)
                    print("Error: ", error)
                    cursor.execute('abort')
        # conn.commit()
        count = cursor.rowcount
        print(count, "record inserted successfully into remakes table")
        # for record in cursor:
        #     print(record)

    except (Exception, psycopg2.Error) as error:
        print("error while connecting to postgresql", error)
    finally:
        if(conn):
            cursor.close()
            conn.close()
    print("ERRORS")
    for error in errors:
        print(error)
main()
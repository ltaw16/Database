# needed for connection
# tutorial website: https://pynative.com/python-postgresql-tutorial/
# psycopg doc: http://initd.org/psycopg/docs/cursor.html#fetch

import psycopg2 as psycopg2

try:
    conn = psycopg2.connect(host="10.90.10.41",
                            database="yikes",
                            user="ltaw16",
                            password="oracle")
                            
    # just testing stuff
    cursor = conn.cursor()
    # stage name, real name, background, type of tole, images, dob, dowstart, dod, dow end,
    # cursor.execute("insert into actor (stage_name, real_name, background, type_of_role, images, dob, dow_start, dod, dow_end) values ('Willie Aames', null, null, 'unknown', null, 1960, null, 1984, null);")
    cursor.execute("select * from actor;")
    cursor.execute("insert into actor values('Willie Aames', NULL, NULL, 'unknown', NULL, 1960, NULL, 1984, NULL);")

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

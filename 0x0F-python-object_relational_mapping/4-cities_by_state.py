#!/usr/bin/python3
""" list all states from database """

if __name__ == "__main__":

    import MySQLdb
    import sys

    if len(sys.argv) == 4:
        username = sys.argv[1]
        upassword = sys.argv[2]
        dbname = sys.argv[3]

        db = MySQLdb.connect(
            host="localhost",
            user=username,
            passwd=upassword,
            db=dbname,
            port=3306)

        cursor = db.cursor()
        squery = """ SELECT cities.id, cities.name, states.name FROM cities INNER JOIN states ON states.id = cities.state_id ORDER BY cities.id ASC"""

        cursor.execute(squery)
        query_rows = cursor.fetchall()
        for row in query_rows:
            print("({}, '{}', '{}')".format(row[0], row[1], row[2]))

        cursor.close()
        db.close()

#!/usr/bin/python3
""" list all states from database """

if __name__ == "__main__":

    import MySQLdb
    import sys

    if len(sys.argv) == 5:
        username = sys.argv[1]
        upassword = sys.argv[2]
        dbname = sys.argv[3]
        stName = sys.argv[4]

        db = MySQLdb.connect(

            host="localhost",
            user=username,
            passwd=upassword,
            db=dbname,
            port=3306)

        cursor = db.cursor()

        cursor.execute(
            "SELECT cities.id, cities.name, states.name FROM cities JOIN states ON cities.state_id = states.id WHERE states.name=%s ORDER BY cities.id ASC;",
            (stName,))
        query_rows = cursor.fetchall()
        rlen = len(query_rows)
        endo = 1
        for row in query_rows:
            if endo < rlen:
                print("{}, ".format(row[1]), end="")
            else:
                print("{}".format(row[1]))
            endo += 1
        cursor.close()
        db.close()

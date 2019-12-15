#!/usr/bin/python3
""" list all states WITH name starting with N from db """

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
        cursor.execute(
            "SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC")
        query_rows = cursor.fetchall()
        for row in query_rows:
            print("({}, '{}'".format(row[0], row[1]))

        cursor.close()
        db.close()

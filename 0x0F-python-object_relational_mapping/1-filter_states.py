#!/usr/bin/python3
"""[script that lists all states with a name starting
    with N (upper N) from the database hbtn_0e_0_usa
"""


if __name__ == "__main__":
    from sys import argv
    import MySQLdb


# This makes a connection to the MySQL database
db = MySQLdb.connect(
    host="localhost", user=argv[1], passwd=argv[2], db=argv[3], port=3306)
"""
 This is a cursor object which allows use to work through
  the same connection in multiple work environments
"""
cur = db.cursor()

cur.execute("SELECT id, name FROM states WHERE\
    name LIKE 'N%' ORDER BY states.id ASC")
# After Select statemtent you use the Fetch all at once method

rows = cur.fetchall()

for row in rows:
    print(row)

# This is cleanup where all open cursors and databases are closed

cur.close()
db.close()

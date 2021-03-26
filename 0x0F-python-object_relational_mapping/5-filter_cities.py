#!/usr/bin/python3
""" This script list all cities from the hbtn_0e_4_usa Database
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
    
    cur.execute("""SELECT cities.name FROM\
        cities INNER JOIN states ON cities.state_id = states.id\
        WHERE states.name = '{}'\
        ORDER BY cities.id ASC""".format(argv[4]))
    # After Select statemtent you use the Fetch all at once method
    
    rows = cur.fetchall()
    
    for i, row in enumerate(rows, start=0):
        if i != 0:
            print(", ", end="")
        print(row[0], end="")
    print("")

# This is cleanup where all open cursors and databases are closed

cur.close()
db.close()

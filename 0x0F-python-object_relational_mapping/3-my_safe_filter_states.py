#!/usr/bin/python3
"""[This is an extention of the task to but to protect from SQL injection
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
    
    cur.execute("""SELECT id, name FROM states WHERE name = %(name)s \
        ORDER BY states.id ASC""", {'name': argv[4]})
    # After Select statemtent you use the Fetch all at once method
    
    rows = cur.fetchall()
    
    for row in rows:
        print(row)
    
    # This is cleanup where all open cursors and databases are closed
    
    cur.close()
    db.close()


import psycopg2

# connect to postgresql
print("connecting DB 'analysis'...", end="\n\n")
conn = psycopg2.connect(database="analysis", user="postgres", password="jackyen0213", host="localhost", port="5432")
cur = conn.cursor()

# show column names
print("column names:")
cur.execute("Select * FROM teachers LIMIT 0;")
#col_names = [desc[0] for desc in curs.description]
col_names = [desc.name for desc in cur.description]
print(col_names, end="\n\n")

print("table data:")
cur.execute("SELECT * FROM teachers;")
rows = cur.fetchall()    # all rows in table
print(rows, end="\n\n")

# commit the SQL command if update the DB
conn.commit()

# close the cursor
cur.close()

# close the connection
conn.close()

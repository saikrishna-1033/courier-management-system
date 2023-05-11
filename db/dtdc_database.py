import sqlite3
import os

db_abs_path = os.path.dirname(os.path.realpath(__file__)) + '/dtdc.db'
conn = sqlite3.connect(db_abs_path)
c = conn.cursor()

c.execute("DROP TABLE IF EXISTS booking")
c.execute("DROP TABLE IF EXISTS clients")


c.execute("""CREATE TABLE booking(
                    id              INTEGER PRIMARY KEY AUTOINCREMENT,
                    booking_date      DATE,
                    pod_no            TEXT,
                    sname             TEXT,
                    rname             TEXT,
                    scontact          INTEGER,
                    rcontact          INTEGER,
                    pincode           INTEGER,
                    location          TEXT,
                    amount            INTEGER
                    


)""")

c.execute("""CREATE TABLE clients(
                    id              INTEGER PRIMARY KEY AUTOINCREMENT,
                    client_Name            TEXT ,
                    billable_status     TEXT,
                    FOREIGN KEY(client_name) REFERENCES booking(sname)
)""")



c.execute("INSERT INTO booking VALUES (1,'06-05-2023','M1073124','Asian Energy','Sushil Mishra','9699766999','7400394459',400071,'Mumbai',1000000)")
c.execute("INSERT INTO clients VALUES (1,'Asian Energy','true')")



conn.commit()
conn.close()

print("Database is created and initialized.")
print("You can see the tables with the show_tables.py script.")

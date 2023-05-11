import sqlite3
import os

db_abs_path = os.path.dirname(os.path.realpath(__file__)) + '/dtdc.db'

print("Options: (booking,clients,all)")
table = input("Show table: ")

conn = sqlite3.connect(db_abs_path)
c = conn.cursor()

def show_booking():
    try:
        items = c.execute("""SELECT
                                i.id, i.booking_date, i.pod_no, i.sname, i.rname, i.scontact, i.rcontact,i.pincode,i.location,i.amount
                             FROM booking AS i 
        """)

        print("Bookings!!")
        print("#############")
        for row in items:
            print("ID:                      ", row[0]),
            print("Booking Date:            ", row[1]),
            print("POD No:                  ", row[2]),
            print("Sender Name:             ", row[3]),
            print("Reciver Name:            ", row[4]),
            print("Sender contact No.:      ", row[5]),
            print("Reciver Contact No.:     ", row[6]),
            print("Pincode.:                ", row[7]),
            print("Location .:              ", row[8]),
            print("Amount  .:               ", row[9]),
            print("\n")
    except:
        print("Something went wrong, please run dtdc_database.py to initialize the database.")
        conn.close()

def show_clients():
    try:
        comments = c.execute("""SELECT c.id,c.client_name,c.billable_status FROM clients AS c
        """)

        print("CLIENTS")
        print("#############")
        for row in comments:
            print("ID:             ", row[0]),
            print("client NAME:        ", row[1]),
            print("BIllable status:     ", row[2])
            print("\n")
    except:
        print("Something went wrong, please run db_init.py to initialize the database.")
        conn.close()

# def show_categories():
#     try:
#         categories = c.execute("SELECT * FROM categories")

#         print("CATEGORIES")
#         print("#############")
#         for row in categories:
#             print("ID:             ", row[0]),
#             print("Name:           ", row[1])
#             print("\n")
#     except:
#         print("Something went wrong, please run db_init.py to initialize the database.")
#         conn.close()

# def show_subcategories():
#     try:
#         subcategories = c.execute("SELECT s.id, s.name, c.name, c.id FROM subcategories AS s INNER JOIN categories AS c ON s.category_id = c.id")
#         print("SUBCATEGORIES")
#         print("#############")
#         for row in subcategories:
#             print("ID:             ", row[0]),
#             print("Name:           ", row[1]),
#             print("Category:       ", row[2], "(", row[3], ")")
#             print("\n")
#     except:
#         print("Something went wrong, please run db_init.py to initialize the database.")
#         conn.close()


if table == "booking":
    show_booking()
elif table == "clients":
    show_clients()
elif table == "all":
    show_booking()
    show_clients()
else:
    print("This option does not exist.")

conn.close()

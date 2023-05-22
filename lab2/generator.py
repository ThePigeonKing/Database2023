import sqlite3
from faker import Faker

# TODO need some serious ID generation rework

# constants
DB_FILENAME = "mtaxy.db"

fake = Faker()

with sqlite3.connect(DB_FILENAME) as conn:
    c = conn.cursor()

    # prepared sql queries
    sql_insert_user = "INSERT INTO Users (FirstName, LastName, Phone, Email, Password) VALUES (?, ?, ?, ?, ?)"
    sql_insert_driver = "INSERT INTO Drivers (FirstName, LastName, Phone, Email, Password, Status, Rating) VALUES (?, ?, ?, ?, ?, ?, ?)"
    sql_insert_car_type = "INSERT INTO CarTypes (TypeName) VALUES (?)"
    sql_insert_car = "INSERT INTO Cars (DriverID, TypeID, Brand, Model, Year, PlateNumber) VALUES (?, ?, ?, ?, ?, ?)"
    sql_insert_order = "INSERT INTO Orders (UserID, DriverID, OrderTime, ArrivalTime, EndTime, Departure, Destination, Cost) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
    sql_insert_review = "INSERT INTO Reviews (UserID, DriverID, OrderID, Rating, Comment) VALUES (?, ?, ?, ?, ?)"

    # Users
    try:
        for _ in range(100):
            c.execute(sql_insert_user,
                      (fake.first_name(), fake.last_name(), fake.phone_number(), fake.email(), fake.password()))
    except sqlite3.Error as e:
        print(f"An error occurred when inserting into Users: {e.args[0]}")

    # Drivers
    try:
        for _ in range(100):
            c.execute(sql_insert_driver,
                      (fake.first_name(), fake.last_name(), fake.phone_number(), fake.email(), fake.password(), 
                       fake.random_element(elements=('Available', 'Unavailable', 'OnTrip')), fake.random_digit()))
    except sqlite3.Error as e:
        print(f"An error occurred when inserting into Drivers: {e.args[0]}")

    # CarTypes
    try:
        car_types = ['Sedan', 'SUV', 'Pickup', 'Minivan']
        for car_type in car_types:
            c.execute(sql_insert_car_type, (car_type,))
    except sqlite3.Error as e:
        print(f"An error occurred when inserting into CarTypes: {e.args[0]}")

    # Cars
    try:
        for _ in range(100):
            c.execute(sql_insert_car,
                      (fake.random_int(min=1, max=100), fake.random_int(min=1, max=4), fake.company(), fake.catch_phrase(), 
                       fake.year(), fake.license_plate()))
    except sqlite3.Error as e:
        print(f"An error occurred when inserting into Cars: {e.args[0]}")

    # Orders
    try:
        for _ in range(100):
            c.execute(sql_insert_order,
                      (fake.random_int(min=1, max=100), fake.random_int(min=1, max=100), fake.date_time_this_year(), 
                       fake.date_time_this_year(), fake.date_time_this_year(), fake.address(), fake.address(), fake.pydecimal(min_value=20, max_value=500, right_digits=2)))
    except sqlite3.Error as e:
        print(f"An error occurred when inserting into Orders: {e.args[0]}")

    # Reviews
    try:
        for _ in range(100):
            c.execute(sql_insert_review,
                      (fake.random_int(min=1, max=100), fake.random_int(min=1, max=100), fake.random_int(min=1, max=100),
                       fake.random_int(min=1, max=5), fake.sentence(nb_words=10)))
    except sqlite3.Error as e:
        print(f"An error occurred when inserting into Reviews: {e.args[0]}")

import sqlite3
from faker import Faker
import random
import os

fake = Faker()

DB_NAME = "mtaxy.db"

# Users
def add_user(cursor, first_name, last_name, phone, email, password):
    cursor.execute("INSERT INTO Users (FirstName, LastName, Phone, Email, Password) VALUES (?, ?, ?, ?, ?)",
                   (first_name, last_name, phone, email, password))

# Drivers
def add_driver(cursor, first_name, last_name, phone, email, password, status, rating):
    cursor.execute("INSERT INTO Drivers (FirstName, LastName, Phone, Email, Password, Status, Rating) VALUES (?, ?, ?, ?, ?, ?, ?)",
                   (first_name, last_name, phone, email, password, status, rating))

# CarTypes
def add_car_type(cursor, type_name):
    cursor.execute("INSERT INTO CarTypes (TypeName) VALUES (?)", (type_name,))

# Cars
def add_car(cursor, driver_id, type_id, brand, model, year, plate_number):
    cursor.execute("INSERT INTO Cars (DriverID, TypeID, Brand, Model, Year, PlateNumber) VALUES (?, ?, ?, ?, ?, ?)",
                   (driver_id, type_id, brand, model, year, plate_number))

# Orders
def add_order(cursor, user_id, driver_id, order_time, arrival_time, end_time, departure, destination, cost):
    cursor.execute("INSERT INTO Orders (UserID, DriverID, OrderTime, ArrivalTime, EndTime, Departure, Destination, Cost) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                   (user_id, driver_id, order_time, arrival_time, end_time, departure, destination, cost))

# Reviews
def add_review(cursor, user_id, driver_id, order_id, rating, comment):
    cursor.execute("INSERT INTO Reviews (UserID, DriverID, OrderID, Rating, Comment) VALUES (?, ?, ?, ?, ?)",
                   (user_id, driver_id, order_id, rating, comment))

def init_db(filename, cursor: sqlite3.Cursor) -> None:
    SQL_FILE = "../lab1/db_init_sqlite.sql"
    with open(SQL_FILE, "r") as fd:
        sql_script = fd.read()
    
    cursor.executescript(sql_script)



if __name__ == "__main__":

    # always delete old db
    try:
        os.remove(DB_NAME)
    except FileNotFoundError:
        pass

    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()

    init_db(DB_NAME, cursor)

    USRS = int(input("Количество Users: "))
    DRVRS = USRS // 5
    CRS = DRVRS
    ORDRS = USRS // 2
    RVWS = USRS*2


    # Users
    for i in range(USRS):
        add_user(cursor, fake.first_name(), fake.last_name(), fake.phone_number(), fake.email(), fake.password())

    # Drivers
    for i in range(DRVRS): 
        add_driver(cursor, fake.first_name(), fake.last_name(), fake.phone_number(), fake.email(), fake.password(), "Available", round(random.uniform(3.0, 5.0), 1))

    # CarTypes
    car_types = ['Sedan', 'SUV', 'Van', 'Convertible']
    for car_type in car_types:
        add_car_type(cursor, car_type)

    # Cars
    for i in range(CRS): 
        driver_id = i + 1
        type_id = (i % 4) + 1
        add_car(cursor, driver_id, type_id, fake.company(), fake.catch_phrase(), fake.year(), fake.license_plate())

    # Orders
    for i in range(ORDRS):
        user_id = i + 1
        driver_id = random.randint(1, DRVRS)
        add_order(cursor, user_id, driver_id, fake.date_time_this_year(), fake.date_time_this_year(), fake.date_time_this_year(), fake.address(), fake.address(), fake.random_int(min=10, max=1500))

    # Reviews
    for i in range(RVWS): 
        user_id = i + 1
        driver_id = (i % DRVRS) + 1
        order_id = i + 1
        add_review(cursor, user_id, driver_id, order_id, fake.random_int(min=1, max=5), fake.sentence())

    connection.commit()
    connection.close()

    print(f"Success! Создано пользователей - {USRS}, водителей - {DRVRS}, машин - {CRS}, заказов - {ORDRS}, отзывов - {RVWS}")

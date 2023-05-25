import sqlite3
from tabulate import tabulate  # type: ignore
from typing import Any


class Query:
    def __init__(self, query: str, name: str):
        self.query = query
        self.name = name

    def execute(self, conn: sqlite3.Connection) -> Any:
        c = conn.cursor()
        c.execute(self.query)
        return [(d[0] for d in c.description)] + c.fetchall()


query_avg_cost = Query(
    query="""SELECT AVG(Orders.Cost) AS AverageCost
FROM Orders
WHERE Orders.UserID = (
    SELECT UserID
    FROM (
        SELECT UserID, COUNT(OrderID) as OrderCount
        FROM Orders
        GROUP BY UserID
        ORDER BY OrderCount DESC
        LIMIT 1
    )
);
""",
    name="Средняя стоимость поездок у пользователя с наибольшим количеством поездок",
)

query_all_cars_users = Query(
    query="""SELECT Users.FirstName, Users.LastName 
FROM Users 
WHERE NOT EXISTS (
    SELECT * FROM CarTypes 
    WHERE NOT EXISTS (
        SELECT Orders.UserID 
        FROM Orders 
        INNER JOIN Cars ON Orders.DriverID = Cars.DriverID 
        WHERE Cars.TypeID = CarTypes.TypeID AND Orders.UserID = Users.UserID)) LIMIT 10;
""",
    name="Пользователи, которые использовали все виды ТС",
)

query_top5_users = Query(
    query="""SELECT Users.FirstName, Users.LastName, AVG(Orders.Cost) AS AverageCost
FROM Users
JOIN Orders ON Users.UserID = Orders.UserID
WHERE Users.UserID IN (
    SELECT UserID
    FROM (
        SELECT Reviews.UserID, AVG(Reviews.Rating) as AvgRating
        FROM Reviews
        GROUP BY Reviews.UserID
        ORDER BY AvgRating DESC
        LIMIT 5
    )
)
GROUP BY Users.UserID;
""",
    name="Средняя стоимость поездок у пользователей с лучшими оценками заказов",
)

query_user1_orders = Query(
    query="""SELECT CarTypes.TypeName, COUNT(Orders.OrderID) as OrderCount
FROM CarTypes
INNER JOIN Cars ON CarTypes.TypeID = Cars.TypeID
INNER JOIN Orders ON Cars.DriverID = Orders.DriverID
GROUP BY CarTypes.TypeID
ORDER BY OrderCount DESC
LIMIT 1;
""",
    name="Какой тип авто наиболее часто используется в поездках",
)

query_top_drivers_by_amount_of_orders = Query(
    query="""SELECT CarTypes.TypeName, AVG(Drivers.Rating) as AverageRating
FROM CarTypes
INNER JOIN Cars ON CarTypes.TypeID = Cars.TypeID
INNER JOIN Drivers ON Cars.DriverID = Drivers.DriverID
GROUP BY CarTypes.TypeID;
""",
    name="Средний рейтинг водителей по типу автомобилей",
)

query_average_cost = Query(
    query="""SELECT Users.FirstName, Users.LastName
FROM Users
WHERE NOT EXISTS (
    SELECT *
    FROM Orders
    INNER JOIN Cars ON Orders.DriverID = Cars.DriverID
    WHERE Orders.UserID = Users.UserID AND Cars.TypeID != (
        SELECT TypeID
        FROM CarTypes
        WHERE TypeName = 'SUV'
    )
);
""",
    name="Пользователи, который заказывали только SUV",
)

query_order_rating_range = Query(
    query="""SELECT Users.FirstName, Users.LastName
FROM Users
WHERE NOT EXISTS (
    SELECT *
    FROM Orders
    INNER JOIN Drivers ON Orders.DriverID = Drivers.DriverID
    WHERE Orders.UserID = Users.UserID AND Drivers.Rating <= 4.5 AND Drivers.Rating >= 4.0
) LIMIT 10;
""",
    name="Пользователи, сделавшие заказ только у водителей с рейтингом [4.0; 4.5]",
)

query_1000rub = Query(
    query="""SELECT Users.FirstName, Users.LastName
FROM Users
WHERE (
    SELECT SUM(Orders.Cost)
    FROM Orders
    WHERE Orders.UserID = Users.UserID
) > 1000 AND (
    SELECT AVG(Reviews.Rating)
    FROM Reviews
    WHERE Reviews.UserID = Users.UserID
) > 4.5 LIMIT 10;
""",
    name="Пользователи, которые потратили в сумме больше 1000 руб. и при этом средний рейтинг их отзывов >4.5",
)

query_most_popular_car_year = Query(
    query="""SELECT Cars.Year, COUNT(Orders.OrderID) AS OrderCount
FROM Cars
INNER JOIN Orders ON Cars.DriverID = Orders.DriverID
GROUP BY Cars.Year
ORDER BY OrderCount DESC
LIMIT 1;
""",
    name="Самый популярный года выпуска автомобилей, используемых в поездках")

if __name__ == "__main__":
    queries = [
        query_avg_cost,
        query_all_cars_users,
        query_top5_users,
        query_user1_orders,
        query_top_drivers_by_amount_of_orders,
        query_average_cost,
        query_order_rating_range,
        query_1000rub,
        query_most_popular_car_year,
    ]

    query_dict = {q.name: q for q in queries}

    conn = sqlite3.connect("mtaxy.db")

    for q in queries:
        print(f"### {q.name}")
        print()
        print(f"Запрос: `{q.query}`")
        print()
        print("```")
        print(tabulate(q.execute(conn)))
        print("```")
        print("\n\n")
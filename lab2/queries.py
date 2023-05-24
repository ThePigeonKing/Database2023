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


query_search_by_email = Query(
    query="SELECT FirstName,LastName FROM Users WHERE Email LIKE '%.com' LIMIT 5;",
    name="Все пользователи с почтой, заканчивающейся на '.com'",
)

query_orders_by_cost = Query(
    query="SELECT COUNT(*) FROM Orders WHERE Cost >= 787.8;",
    name="Количество заказов стоимостью больше 787.8 руб.",
)

query_revies_by_rating = Query(
    query="SELECT Rating, Count(*) FROM Reviews GROUP BY Rating;",
    name="Количество отзывов по оценкам",
)

query_user1_orders = Query(
    query="SELECT COUNT(*) FROM Orders WHERE UserID = 1;",
    name="Количество заказов пользователя с ID = 1",
)

query_top_drivers_by_amount_of_orders = Query(
    query="SELECT FirstName, LastName, Count(*) as n_orders FROM Orders JOIN Drivers ON Orders.DriverID = Drivers.DriverID GROUP BY FirstName, LastName ORDER BY n_orders desc LIMIT 5;",
    name="Топ водителей по количеству заказов",
)

query_average_cost = Query(
    query="SELECT AVG(Cost) FROM Orders;",
    name="Средняя стоимость заказа такси",
)

query_cost_timeperiod = Query(
    query="SELECT SUM(Cost) FROM Orders WHERE OrderTime BETWEEN '2023-05-01 00:00:00' AND '2023-08-01 23:59:59';",
    name="Сумма запросов за определенный период времени",
)

query_car_current_type = Query(
    query="SELECT * FROM Cars WHERE TypeID = (SELECT TypeID FROM CarTypes WHERE TypeName = 'SUV');",
    name="Все автомобили определенного типа",
)

query_users_without_orders = Query(
    query="SELECT * FROM Users WHERE UserID NOT IN (SELECT UserID FROM Orders) LIMIT 10;",
    name="Пользователи, которые ещё не сделали ни одного заказа",
)

if __name__ == "__main__":
    queries = [
        query_average_cost,
        query_car_current_type,
        query_user1_orders,
        query_revies_by_rating,
        query_users_without_orders,
        query_orders_by_cost,
        query_search_by_email,
        query_cost_timeperiod,
        query_top_drivers_by_amount_of_orders,
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
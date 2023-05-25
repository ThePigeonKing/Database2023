# НИЯУ МИФИ. ИИКС. Лабораторная работа #1 
## Полищук Максим, Б20-505

### Генерация тестовых данных
Создан несложный скрипт для создания тестовых данных

Использование:
```bash
python3 gen.py
```
В результате работы файлы будет создан файл `mtaxy.db` (скрипт основан на .sql файле из первой лабораторной)


### Запросы

#### Средняя стоимость поездок у пользователя с наибольшим количеством поездок

Запрос: `SELECT AVG(Orders.Cost) AS AverageCost
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
`

```
-----------------
AverageCost
740.8571428571429
-----------------
```



#### Пользователи, которые использовали все виды ТС

Запрос: `SELECT Users.FirstName, Users.LastName
FROM Users
WHERE NOT EXISTS (
    SELECT * FROM CarTypes
    WHERE NOT EXISTS (
        SELECT Orders.UserID
        FROM Orders
        INNER JOIN Cars ON Orders.DriverID = Cars.DriverID
        WHERE Cars.TypeID = CarTypes.TypeID AND Orders.UserID = Users.UserID)) LIMIT 10;
`

```
---------  ---------
FirstName  LastName
Theresa    Sparks
Amy        Johnson
Sonya      Harris
Victor     Winters
Brandon    Flores
Sandra     Thomas
Randall    Carpenter
Emily      Scott
Rebecca    Nolan
Shannon    Ellis
---------  ---------
```



#### Средняя стоимость поездок у пользователей с лучшими оценками заказов

Запрос: `SELECT Users.FirstName, Users.LastName, AVG(Orders.Cost) AS AverageCost
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
`

```
---------  ---------  -----------------
FirstName  LastName   AverageCost
Anthony    Gutierrez  956.25
Brooke     Mitchell   726.6666666666666
Brandy     Hartman    1365.5
Patrick    Gonzalez   745.5
Jason      Turner     696.0
---------  ---------  -----------------
```



#### Какой тип авто наиболее часто используется в поездках

Запрос: `SELECT CarTypes.TypeName, COUNT(Orders.OrderID) as OrderCount
FROM CarTypes
INNER JOIN Cars ON CarTypes.TypeID = Cars.TypeID
INNER JOIN Orders ON Cars.DriverID = Orders.DriverID
GROUP BY CarTypes.TypeID
ORDER BY OrderCount DESC
LIMIT 1;
`

```
--------  ----------
TypeName  OrderCount
SUV       635
--------  ----------
```



#### Средний рейтинг водителей по типу автомобилей

Запрос: `SELECT CarTypes.TypeName, AVG(Drivers.Rating) as AverageRating
FROM CarTypes
INNER JOIN Cars ON CarTypes.TypeID = Cars.TypeID
INNER JOIN Drivers ON Cars.DriverID = Drivers.DriverID
GROUP BY CarTypes.TypeID;
`

```
-----------  ------------------
TypeName     AverageRating
Sedan        4.276000000000001
SUV          3.9760000000000004
Van          3.9479999999999995
Convertible  4.036000000000001
-----------  ------------------
```



#### Пользователи, который заказывали только SUV

Запрос: `SELECT Users.FirstName, Users.LastName
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
`

```
---------  ---------
FirstName  LastName
Brian      Williams
Lisa       Reynolds
Ashley     Thomas
Amy        Welch
Ian        Schultz
Robert     Castaneda
Natalie    Lucas
Jennifer   Ayala
Jason      Patrick
Ronald     Ewing
---------  ---------
```



#### Пользователи, сделавшие заказ только у водителей с рейтингом [4.0; 4.5]

Запрос: `SELECT Users.FirstName, Users.LastName
FROM Users
WHERE NOT EXISTS (
    SELECT *
    FROM Orders
    INNER JOIN Drivers ON Orders.DriverID = Drivers.DriverID
    WHERE Orders.UserID = Users.UserID AND Drivers.Rating <= 4.5 AND Drivers.Rating >= 4.0
) LIMIT 10;
`

```
-----------  --------
FirstName    LastName
Brandon      Flores
Rachel       Walker
Joshua       White
Christopher  Cooper
Michelle     Villa
Jennifer     Simmons
Cody         Simmons
Timothy      Green
Renee        Ramirez
Donald       Robles
-----------  --------
```



#### Пользователи, которые потратили в сумме больше 1000 руб. и при этом средний рейтинг их отзывов >4.5

Запрос: `SELECT Users.FirstName, Users.LastName
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
`

```
---------  ---------
FirstName  LastName
Teresa     Franklin
Amy        Johnson
Brandon    Flores
Rachel     Walker
Sandra     Thomas
Donna      Gordon
Cody       Olson
Lawrence   Scott
Lisa       Schroeder
Marc       Kirk
---------  ---------
```



#### Самый популярный года выпуска автомобилей, используемых в поездках

Запрос: `SELECT Cars.Year, COUNT(Orders.OrderID) AS OrderCount
FROM Cars
INNER JOIN Orders ON Cars.DriverID = Orders.DriverID
GROUP BY Cars.Year
ORDER BY OrderCount DESC
LIMIT 1;
`

```
----  ----------
Year  OrderCount
1980  112
----  ----------
```

### Приложение

[Запросы](./queries.py)

## Заключение

Были разработаны более сложные запросы к разработанной БД.
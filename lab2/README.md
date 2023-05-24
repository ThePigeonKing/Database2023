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

#### Средняя стоимость заказа такси

Запрос: `SELECT AVG(Cost) FROM Orders;`

```
---------
AVG(Cost)
720.04
---------
```



#### Все автомобили определенного типа

Запрос: `SELECT * FROM Cars WHERE TypeID = (SELECT TypeID FROM CarTypes WHERE TypeName = 'SUV');`

```
-----  --------  ------  --------------------------  -----------------------------------------  ----  -----------
CarID  DriverID  TypeID  Brand                       Model                                      Year  PlateNumber
2      2         2       Miller Group                Extended tertiary website                  1988  KWM 817
6      6         2       Jordan Ltd                  Advanced coherent artificial intelligence  1976  903 THC
10     10        2       Dunlap, Ortiz and Bennett   Automated client-server circuit            1996  QGA-3154
14     14        2       Carrillo, Foster and Moore  Re-contextualized regional protocol        1973  704 TQH
18     18        2       Massey, Bentley and Wang    Implemented tangible superstructure        1974  YGE4672
-----  --------  ------  --------------------------  -----------------------------------------  ----  -----------
```



#### Количество заказов пользователя с ID = 1

Запрос: `SELECT COUNT(*) FROM Orders WHERE UserID = 1;`

```
--------
COUNT(*)
1
--------
```



#### Количество отзывов по оценкам

Запрос: `SELECT Rating, Count(*) FROM Reviews GROUP BY Rating;`

```
------  --------
Rating  Count(*)
1.0     49
2.0     34
3.0     37
4.0     37
5.0     43
------  --------
```



#### Пользователи, которые ещё не сделали ни одного заказа

Запрос: `SELECT * FROM Users WHERE UserID NOT IN (SELECT UserID FROM Orders) LIMIT 10;`

```
------  ---------  ---------  ---------------------  --------------------------  ----------
UserID  FirstName  LastName   Phone                  Email                       Password
51      David      Miller     +1-195-563-8203x2786   mchristensen@example.net    ^87YTe+ndA
52      Sylvia     Lang       3857674849             browncourtney@example.com   s+0WjWMy4P
53      Tyler      Snyder     326.386.2705           antonio20@example.com       @yuYJP4XA4
54      Mary       Schroeder  977-940-0532x57249     gregoryfrazier@example.com  0%^Eupml+2
55      Joseph     Jensen     (389)040-3099x911      normanbrian@example.com     s$^4Tnsg4l
56      Andrew     Cook       001-027-636-6072x997   burtonkaitlyn@example.org   cZ#0InkTRj
57      Samantha   Marquez    079.988.1852x564       brittanytran@example.com    4)V4Efdu5%
58      Richard    Jones      +1-883-408-6993x48375  burchnancy@example.org      !SVrTVld!0
59      Phyllis    Jackson    1120042036             wgray@example.org           )4JMch_u6j
60      Joseph     Maxwell    805-356-0793x6560      mitchell91@example.com      8q6XzYqI%@
------  ---------  ---------  ---------------------  --------------------------  ----------
```



#### Количество заказов стоимостью больше 787.8 руб.

Запрос: `SELECT COUNT(*) FROM Orders WHERE Cost >= 787.8;`

```
--------
COUNT(*)
22
--------
```



#### Все пользователи с почтой, заканчивающейся на '.com'

Запрос: `SELECT FirstName,LastName FROM Users WHERE Email LIKE '%.com' LIMIT 5;`

```
---------  ---------
FirstName  LastName
Sherry     Allen
Rebekah    Henderson
Jonathan   Garcia
Lisa       Walker
John       Lopez
---------  ---------
```



#### Сумма запросов за определенный период времени

Запрос: `SELECT SUM(Cost) FROM Orders WHERE OrderTime BETWEEN '2023-05-01 00:00:00' AND '2023-08-01 23:59:59';`

```
---------
SUM(Cost)
8664.0
---------
```



#### Топ водителей по количеству заказов

Запрос: `SELECT FirstName, LastName, Count(*) as n_orders FROM Orders JOIN Drivers ON Orders.DriverID = Drivers.DriverID GROUP BY FirstName, LastName ORDER BY n_orders desc LIMIT 5;`

```
---------  --------  --------
FirstName  LastName  n_orders
Carl       Preston   6
Julie      Walton    6
Jared      Merritt   4
Stephanie  Vargas    4
Steven     Cox       4
---------  --------  --------
```

### Повторить запросы на своих данных
Для этого был разработан сценарий `queries.py`; запуск этого сценария выведет результаты работы приведенных выше запросов на файле `mtaxy.db`. Внешняя зависимость: `tabulate`

```python3
python3 queries.py
```

Было ~~украдено~~ вдохновлено @ne_bknn ([link](https://github.com/ne-bknn/dbms_labs/blob/master/02_lab/queries.py))

### Приложение
[Генератор](./gen.py)  
[Запросы](./queries.py)

### Заключение
# Заключение

Был разработан сценарий для генерации тестовых данных и ряд запросов для получения актуальной информации для заданной предметной области.

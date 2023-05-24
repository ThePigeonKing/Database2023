CREATE TABLE Users (
    UserID INTEGER PRIMARY KEY AUTOINCREMENT,
    FirstName TEXT,
    LastName TEXT,
    Phone TEXT,
    Email TEXT UNIQUE,
    Password TEXT
);

CREATE TABLE Drivers (
    DriverID INTEGER PRIMARY KEY AUTOINCREMENT,
    FirstName TEXT,
    LastName TEXT,
    Phone TEXT,
    Email TEXT UNIQUE,
    Password TEXT,
    Status TEXT,
    Rating REAL
);

CREATE TABLE CarTypes (
    TypeID INTEGER PRIMARY KEY AUTOINCREMENT,
    TypeName TEXT
);

CREATE TABLE Cars (
    CarID INTEGER PRIMARY KEY AUTOINCREMENT,
    DriverID INTEGER,
    TypeID INTEGER,
    Brand TEXT,
    Model TEXT,
    Year INTEGER,
    PlateNumber TEXT,
    FOREIGN KEY(DriverID) REFERENCES Drivers(DriverID),
    FOREIGN KEY(TypeID) REFERENCES CarTypes(TypeID)
);

CREATE TABLE Orders (
    OrderID INTEGER PRIMARY KEY AUTOINCREMENT,
    UserID INTEGER,
    DriverID INTEGER,
    OrderTime TEXT,
    ArrivalTime TEXT,
    EndTime TEXT,
    Departure TEXT,
    Destination TEXT,
    Cost REAL,
    FOREIGN KEY(UserID) REFERENCES Users(UserID),
    FOREIGN KEY(DriverID) REFERENCES Drivers(DriverID)
);

CREATE TABLE Reviews (
    ReviewID INTEGER PRIMARY KEY AUTOINCREMENT,
    UserID INTEGER,
    DriverID INTEGER,
    OrderID INTEGER,
    Rating REAL,
    Comment TEXT,
    FOREIGN KEY(UserID) REFERENCES Users(UserID),
    FOREIGN KEY(DriverID) REFERENCES Drivers(DriverID),
    FOREIGN KEY(OrderID) REFERENCES Orders(OrderID)
);

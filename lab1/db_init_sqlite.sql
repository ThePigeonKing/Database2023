CREATE TABLE Users (
    UserID TEXT PRIMARY KEY,
    FirstName TEXT,
    LastName TEXT,
    Phone TEXT,
    Email TEXT UNIQUE,
    Password TEXT -- should be hashed
);

CREATE TABLE Drivers (
    DriverID TEXT PRIMARY KEY,
    FirstName TEXT,
    LastName TEXT,
    Phone TEXT,
    Email TEXT UNIQUE,
    Password TEXT, -- should be hashed
    Status TEXT,
    Rating REAL
);

CREATE TABLE Cars (
    CarID TEXT PRIMARY KEY,
    DriverID TEXT,
    Brand TEXT,
    Model TEXT,
    Year INT,
    PlateNumber TEXT,
    FOREIGN KEY (DriverID) REFERENCES Drivers(DriverID)
);

CREATE TABLE Orders (
    OrderID TEXT PRIMARY KEY,
    UserID TEXT,
    DriverID TEXT,
    OrderTime TEXT,
    ArrivalTime TEXT,
    EndTime TEXT,
    Departure TEXT,
    Destination TEXT,
    Cost REAL,
    FOREIGN KEY (UserID) REFERENCES Users(UserID),
    FOREIGN KEY (DriverID) REFERENCES Drivers(DriverID)
);

CREATE TABLE Reviews (
    ReviewID TEXT PRIMARY KEY,
    UserID TEXT,
    DriverID TEXT,
    OrderID TEXT,
    Rating REAL,
    Comment TEXT,
    FOREIGN KEY (UserID) REFERENCES Users(UserID),
    FOREIGN KEY (DriverID) REFERENCES Drivers(DriverID),
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID)
);

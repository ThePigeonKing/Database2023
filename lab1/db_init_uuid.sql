CREATE EXTENSION IF NOT EXISTS "uuid-ossp"; -- to generate UUIDs

CREATE TABLE Users (
    UserID UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
    FirstName VARCHAR(100),
    LastName VARCHAR(100),
    Phone VARCHAR(15),
    Email VARCHAR(100) UNIQUE,
    Password VARCHAR(255) -- should be hashed
);

CREATE TABLE Drivers (
    DriverID UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
    FirstName VARCHAR(100),
    LastName VARCHAR(100),
    Phone VARCHAR(15),
    Email VARCHAR(100) UNIQUE,
    Password VARCHAR(255), -- should be hashed
    Status VARCHAR(50),
    Rating DECIMAL(2,1)
);

CREATE TABLE Cars (
    CarID UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
    DriverID UUID,
    Brand VARCHAR(50),
    Model VARCHAR(50),
    Year INT,
    PlateNumber VARCHAR(15),
    FOREIGN KEY (DriverID) REFERENCES Drivers(DriverID)
);

CREATE TABLE Orders (
    OrderID UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
    UserID UUID,
    DriverID UUID,
    OrderTime TIMESTAMP,
    ArrivalTime TIMESTAMP,
    EndTime TIMESTAMP
CREATE EXTENSION IF NOT EXISTS "uuid-ossp"; -- to generate UUIDs

CREATE TABLE Users (
    UserID UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
    FirstName VARCHAR(100),
    LastName VARCHAR(100),
    Phone VARCHAR(15),
    Email VARCHAR(100) UNIQUE,
    Password VARCHAR(255) -- should be hashed
);

CREATE TABLE Drivers (
    DriverID UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
    FirstName VARCHAR(100),
    LastName VARCHAR(100),
    Phone VARCHAR(15),
    Email VARCHAR(100) UNIQUE,
    Password VARCHAR(255), -- should be hashed
    Status VARCHAR(50),
    Rating DECIMAL(2,1)
);

CREATE TABLE Cars (
    CarID UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
    DriverID UUID,
    Brand VARCHAR(50),
    Model VARCHAR(50),
    Year INT,
    PlateNumber VARCHAR(15),
    FOREIGN KEY (DriverID) REFERENCES Drivers(DriverID)
);

CREATE TABLE Orders (
    OrderID UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
    UserID UUID,
    DriverID UUID,
    OrderTime TIMESTAMP,
    ArrivalTime TIMESTAMP,
    EndTime TIMESTAMP,
    Departure VARCHAR(255),
    Destination VARCHAR(255),
    Cost DECIMAL(7,2),
    FOREIGN KEY (UserID) REFERENCES Users(UserID),
    FOREIGN KEY (DriverID) REFERENCES Drivers(DriverID)
);

CREATE TABLE Reviews (
    ReviewID UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
    UserID UUID,
    DriverID UUID,
    OrderID UUID,
    Rating DECIMAL(2,1),
    Comment TEXT,
    FOREIGN KEY (UserID) REFERENCES Users(UserID),
    FOREIGN KEY (DriverID) REFERENCES Drivers(DriverID),
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID)
);

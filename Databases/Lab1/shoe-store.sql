CREATE TABLE Product (
	CodeProduct integer PRIMARY KEY AUTOINCREMENT,
	Name varchar,
	SizeProduct float,
	Brand varchar,
	Material varchar,
	Gender varchar,
	Color varchar
);

CREATE TABLE Orderr (
	CodeOrder integer PRIMARY KEY AUTOINCREMENT,
	CodeBuyer integer,
	CodeEmployee integer,
	DateOrder date
);

CREATE TABLE Buyer (
	CodeBuyer integer PRIMARY KEY AUTOINCREMENT,
	Surname varchar,
	Name varchar,
	Patronymic varchar,
	Number integer,
	Email varchar,
	Country varchar,
	City varchar,
	Address varchar
);

CREATE TABLE Employee (
	CodeEmployee integer PRIMARY KEY AUTOINCREMENT,
	Surname varchar,
	Name varchar,
	PositionEmployee varchar
);

CREATE TABLE Ordered (
	CodeOrdered integer PRIMARY KEY AUTOINCREMENT,
	CodeOrder integer,
	CodeProduct integer,
	Quantity integer,
	Price float
);


INSERT INTO Orderr (DateOrder)
VALUES ('15.10.2004');

INSERT INTO Buyer (Surname, Name)
VALUES ('Ilyakhova', 'Alice');


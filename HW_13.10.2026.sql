-- Домашнє завдання 13.10.2026 (MS SQL Server, T-SQL)

-- #1 Тритаблична база даних Sales
CREATE DATABASE Sales;
GO

USE Sales;
GO

CREATE TABLE Salesmen (
    Id          INT IDENTITY(1, 1) NOT NULL PRIMARY KEY,
    FirstName   NVARCHAR(50) NOT NULL CHECK (FirstName <> N''),
    LastName    NVARCHAR(50) NOT NULL CHECK (LastName <> N''),
    Phone       NVARCHAR(20) NULL
);
GO

CREATE TABLE Customers (
    Id          INT IDENTITY(1, 1) NOT NULL PRIMARY KEY,
    FirstName   NVARCHAR(50) NOT NULL CHECK (FirstName <> N''),
    LastName    NVARCHAR(50) NOT NULL CHECK (LastName <> N''),
    Email       NVARCHAR(100) NULL
);
GO

CREATE TABLE Sales (
    Id          INT IDENTITY(1, 1) NOT NULL PRIMARY KEY,
    SalesmanId  INT NOT NULL REFERENCES Salesmen (Id),
    CustomerId  INT NOT NULL REFERENCES Customers (Id),
    Product     NVARCHAR(100) NOT NULL,
    Amount      MONEY NOT NULL CHECK (Amount > 0),
    SaleDate    DATE NOT NULL DEFAULT GETDATE()
);
GO

INSERT INTO Salesmen (FirstName, LastName, Phone)
VALUES (N'Олег',   N'Шевченко', N'+380501112233'),
       (N'Ірина',  N'Мельник',  N'+380672223344'),
       (N'Андрій', N'Бондар',   NULL);

INSERT INTO Customers (FirstName, LastName, Email)
VALUES (N'Іван',   N'Петренко',  N'ivan@gmail.com'),
       (N'Олена',  N'Коваль',    N'olena@gmail.com'),
       (N'Максим', N'Сидоренко', NULL);

INSERT INTO Sales (SalesmanId, CustomerId, Product, Amount, SaleDate)
VALUES (1, 1, N'Ноутбук',    32000, '2026-09-01'),
       (1, 2, N'Мишка',        800, '2026-09-03'),
       (2, 1, N'Монітор',    9500, '2026-09-05'),
       (2, 3, N'Клавіатура',  2100, '2026-09-10'),
       (3, 2, N'Смартфон',   21000, '2026-09-12'),
       (1, 3, N'Навушники',   3500, '2026-09-15'),
       (3, 1, N'Планшет',    15000, '2026-09-20');
GO

-- Конкретний продавець і покупець для запитів
DECLARE @SalesmanId INT = 1;   -- Олег Шевченко
DECLARE @CustomerId INT = 1;   -- Іван Петренко

-- 1. Відображення усіх угод
SELECT s.Id, sm.FirstName + N' ' + sm.LastName AS Salesman,
       c.FirstName + N' ' + c.LastName AS Customer,
       s.Product, s.Amount, s.SaleDate
FROM Sales s
JOIN Salesmen sm ON sm.Id = s.SalesmanId
JOIN Customers c ON c.Id = s.CustomerId;

-- 2. Відображення угод конкретного продавця
SELECT s.Id, c.FirstName + N' ' + c.LastName AS Customer, s.Product, s.Amount, s.SaleDate
FROM Sales s
JOIN Customers c ON c.Id = s.CustomerId
WHERE s.SalesmanId = @SalesmanId;

-- 3. Відображення максимальної за сумою угоди
SELECT TOP 1 WITH TIES *
FROM Sales
ORDER BY Amount DESC;

-- 4. Відображення мінімальної за сумою угоди
SELECT TOP 1 WITH TIES *
FROM Sales
ORDER BY Amount ASC;

-- 5. Відображення максимальної суми угоди для конкретного продавця
SELECT MAX(Amount) AS MaxAmount
FROM Sales
WHERE SalesmanId = @SalesmanId;

-- 6. Відображення мінімальної за сумою угоди для конкретного продавця
SELECT TOP 1 WITH TIES *
FROM Sales
WHERE SalesmanId = @SalesmanId
ORDER BY Amount ASC;

-- 7. Відображення максимальної за сумою угоди для конкретного покупця
SELECT TOP 1 WITH TIES *
FROM Sales
WHERE CustomerId = @CustomerId
ORDER BY Amount DESC;

-- 8. Відображення мінімальної за сумою угоди для конкретного покупця
SELECT TOP 1 WITH TIES *
FROM Sales
WHERE CustomerId = @CustomerId
ORDER BY Amount ASC;

-- 9. Відображення продавця з максимальною сумою продажів за всіма угодами
SELECT TOP 1 WITH TIES sm.Id, sm.FirstName, sm.LastName, SUM(s.Amount) AS TotalSales
FROM Salesmen sm
JOIN Sales s ON s.SalesmanId = sm.Id
GROUP BY sm.Id, sm.FirstName, sm.LastName
ORDER BY TotalSales DESC;

-- 10. Відображення продавця з мінімальною сумою продажів за всіма угодами
SELECT TOP 1 WITH TIES sm.Id, sm.FirstName, sm.LastName, SUM(s.Amount) AS TotalSales
FROM Salesmen sm
JOIN Sales s ON s.SalesmanId = sm.Id
GROUP BY sm.Id, sm.FirstName, sm.LastName
ORDER BY TotalSales ASC;

-- 11. Відображення покупця з максимальною сумою покупок за всіма угодами
SELECT TOP 1 WITH TIES c.Id, c.FirstName, c.LastName, SUM(s.Amount) AS TotalPurchases
FROM Customers c
JOIN Sales s ON s.CustomerId = c.Id
GROUP BY c.Id, c.FirstName, c.LastName
ORDER BY TotalPurchases DESC;

-- 12. Відображення середньої суми покупки для конкретного покупця
SELECT c.FirstName, c.LastName, AVG(s.Amount) AS AvgPurchase
FROM Customers c
JOIN Sales s ON s.CustomerId = c.Id
WHERE c.Id = @CustomerId
GROUP BY c.FirstName, c.LastName;

-- 13. Відображення середньої суми покупки для конкретного продавця
SELECT sm.FirstName, sm.LastName, AVG(s.Amount) AS AvgSale
FROM Salesmen sm
JOIN Sales s ON s.SalesmanId = sm.Id
WHERE sm.Id = @SalesmanId
GROUP BY sm.FirstName, sm.LastName;
GO

-- Домашнє завдання 06.10.2026 (MS SQL Server, T-SQL)

-- #1 База для зберігання оцінок студентів
CREATE DATABASE StudentsGrades;
GO

USE StudentsGrades;
GO

CREATE TABLE StudentGrades (
    Id                  INT IDENTITY(1, 1) NOT NULL PRIMARY KEY,
    FullName            NVARCHAR(150) NOT NULL CHECK (FullName <> N''),
    City                NVARCHAR(100) NOT NULL,
    Country             NVARCHAR(100) NOT NULL,
    BirthDate           DATE NOT NULL,
    Email               NVARCHAR(100) NOT NULL UNIQUE,
    Phone               NVARCHAR(20) NULL,
    GroupName           NVARCHAR(20) NOT NULL,
    AverageGrade        DECIMAL(4, 2) NOT NULL CHECK (AverageGrade BETWEEN 0 AND 12),
    MinAvgSubject       NVARCHAR(100) NOT NULL,   -- предмет з мінімальною середньою оцінкою
    MaxAvgSubject       NVARCHAR(100) NOT NULL    -- предмет з максимальною середньою оцінкою
);
GO

INSERT INTO StudentGrades (FullName, City, Country, BirthDate, Email, Phone, GroupName,
                           AverageGrade, MinAvgSubject, MaxAvgSubject)
VALUES
    (N'Петренко Іван Олегович',   N'Київ',  N'Україна', '2007-03-14', N'ivan.p@gmail.com',   N'+380501112233', N'PY-31', 10.40, N'Фізика',      N'Програмування'),
    (N'Коваль Олена Андріївна',   N'Львів', N'Україна', '2006-11-02', N'olena.k@gmail.com',  N'+380672223344', N'PY-31', 11.20, N'Історія',     N'Англійська мова'),
    (N'Сидоренко Максим Ігорович', N'Одеса', N'Україна', '2007-07-21', N'max.s@gmail.com',    NULL,             N'WEB-12', 8.75, N'Математика',  N'Веб-дизайн');
GO

SELECT * FROM StudentGrades;
GO


-- #2 База даних Лікарня (Hospital)
CREATE DATABASE Hospital;
GO

USE Hospital;
GO

-- Відділення
CREATE TABLE Departments (
    Id          INT IDENTITY(1, 1) NOT NULL PRIMARY KEY,
    Building    INT NOT NULL CHECK (Building BETWEEN 1 AND 5),
    Financing   MONEY NOT NULL DEFAULT 0 CHECK (Financing >= 0),
    Name        NVARCHAR(100) NOT NULL UNIQUE CHECK (Name <> N'')
);
GO

-- Захворювання
CREATE TABLE Diseases (
    Id          INT IDENTITY(1, 1) NOT NULL PRIMARY KEY,
    Name        NVARCHAR(100) NOT NULL UNIQUE CHECK (Name <> N''),
    Severity    INT NOT NULL DEFAULT 1 CHECK (Severity >= 1)
);
GO

-- Лікарі
CREATE TABLE Doctors (
    Id          INT IDENTITY(1, 1) NOT NULL PRIMARY KEY,
    Name        NVARCHAR(MAX) NOT NULL CHECK (Name <> N''),
    Phone       CHAR(10) NULL,
    Salary      MONEY NOT NULL CHECK (Salary > 0),
    Surname     NVARCHAR(MAX) NOT NULL CHECK (Surname <> N'')
);
GO

-- Обстеження
CREATE TABLE Examinations (
    Id          INT IDENTITY(1, 1) NOT NULL PRIMARY KEY,
    DayOfWeek   INT NOT NULL CHECK (DayOfWeek BETWEEN 1 AND 7),
    EndTime     TIME NOT NULL,
    Name        NVARCHAR(100) NOT NULL UNIQUE CHECK (Name <> N''),
    StartTime   TIME NOT NULL CHECK (StartTime BETWEEN '08:00' AND '18:00'),
    CONSTRAINT CK_Examinations_EndTime CHECK (EndTime > StartTime)
);
GO

-- Палати
CREATE TABLE Wards (
    Id          INT IDENTITY(1, 1) NOT NULL PRIMARY KEY,
    Building    INT NOT NULL CHECK (Building BETWEEN 1 AND 5),
    Floor       INT NOT NULL CHECK (Floor >= 1),
    Name        NVARCHAR(20) NOT NULL UNIQUE CHECK (Name <> N'')
);
GO

-- Тестові дані
INSERT INTO Departments (Building, Financing, Name)
VALUES (1, 150000, N'Кардіологія'),
       (2, 120000, N'Неврологія'),
       (3, 0,      N'Терапія');

INSERT INTO Diseases (Name, Severity)
VALUES (N'Грип', 2),
       (N'Гіпертонія', 3),
       (N'Застуда', DEFAULT);

INSERT INTO Doctors (Name, Surname, Phone, Salary)
VALUES (N'Олег',  N'Шевченко', '0501234567', 25000),
       (N'Ірина', N'Мельник',  NULL,         28000);

INSERT INTO Examinations (DayOfWeek, StartTime, EndTime, Name)
VALUES (1, '09:00', '10:00', N'Кардіограма'),
       (3, '14:30', '15:00', N'Аналіз крові'),
       (5, '17:00', '18:30', N'МРТ');

INSERT INTO Wards (Building, Floor, Name)
VALUES (1, 2, N'Палата 201'),
       (2, 1, N'Палата 105');
GO

-- Перевірка обмежень: кожен з цих запитів має завершитися помилкою CHECK/UNIQUE
-- INSERT INTO Departments (Building, Name) VALUES (6, N'Хірургія');               -- корпус поза 1..5
-- INSERT INTO Diseases (Name, Severity) VALUES (N'Грип', 1);                      -- назва не унікальна
-- INSERT INTO Doctors (Name, Surname, Salary) VALUES (N'Петро', N'Іванов', 0);    -- ставка <= 0
-- INSERT INTO Examinations (DayOfWeek, StartTime, EndTime, Name)
--     VALUES (2, '07:30', '08:00', N'УЗД');                                       -- початок раніше 8:00
-- INSERT INTO Examinations (DayOfWeek, StartTime, EndTime, Name)
--     VALUES (2, '12:00', '11:00', N'Рентген');                                   -- кінець раніше початку
-- INSERT INTO Wards (Building, Floor, Name) VALUES (1, 0, N'Палата 001');         -- поверх < 1

SELECT * FROM Departments;
SELECT * FROM Diseases;
SELECT * FROM Doctors;
SELECT * FROM Examinations;
SELECT * FROM Wards;
GO

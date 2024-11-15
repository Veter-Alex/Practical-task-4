import sqlite3


def create_tables():
    """Используя команду CREATE DATABASE,
    создайте новую базу данных с названием,
    которое отражает ее цель (например, SchoolDB для базы данных школы).

    Используя команду CREATE TABLE,
    создайте несколько таблиц
    (например, таблицы Students, Courses, Enrollments).
    Укажите основные поля, такие как id, name
    и необходимые типы данных.
    """

    conn = sqlite3.connect("SchoolDB.db")
    cursor = conn.cursor()
    # создаем таблицу студентов
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS Students (
            StudentID INTEGER PRIMARY KEY AUTOINCREMENT,
            Name TEXT NOT NULL,
            Age INTEGER NOT NULL,
            Gender TEXT NOT NULL,
            EnrollmentDate TEXT NOT NULL
        )"""
    )

    # создаем таблицу курсов
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS Courses (
            CourseID INTEGER PRIMARY KEY AUTOINCREMENT,
            CourseName TEXT NOT NULL,
            DurationWeeks INTEGER NOT NULL,
            StartDate TEXT NOT NULL
        )"""
    )

    # создаем таблицу связи студентов и курсов
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS Enrollments (
            EnrollmentID INTEGER PRIMARY KEY AUTOINCREMENT,
            StudentID INTEGER NOT NULL,
            CourseID INTEGER NOT NULL,
            EnrollmentDate TEXT NOT NULL,
            FOREIGN KEY (StudentID) REFERENCES Students (StudentID),
            FOREIGN KEY (CourseID) REFERENCES Courses (CourseID)
        )"""
    )

    conn.commit()
    conn.close()


def insert_sample_data():
    """Используйте команду INSERT INTO,
    чтобы добавить несколько записей в каждую из созданных таблиц.
    """

    conn = sqlite3.connect("SchoolDB.db")
    cursor = conn.cursor()
    # вставляем данные в таблицу студентов
    cursor.executemany(
        "INSERT INTO Students (Name, Age, Gender, EnrollmentDate) VALUES (?, ?, ?, ?)",
        [
            ("Alice", 20, "Female", "2022-01-01"),
            ("Bob", 20, "Male", "2022-02-01"),
            ("Charlie", 22, "Female", "2022-03-01"),
            ("David", 20, "Male", "2022-04-01"),
            ("Eva", 24, "Female", "2022-05-01"),
        ],
    )

    # вставляем данные в таблицу курсов
    cursor.executemany(
        "INSERT INTO Courses (CourseName, DurationWeeks, StartDate) VALUES (?, ?, ?)",
        [
            ("Math", 12, "2022-01-01"),
            ("English", 12, "2022-02-01"),
            ("Science", 12, "2022-03-01"),
            ("History", 8, "2022-04-01"),
            ("Art", 6, "2022-05-01"),
        ],
    )

    # вставляем данные в таблицу связи студентов и курсов
    cursor.executemany(
        "INSERT INTO Enrollments (StudentID, CourseID, EnrollmentDate) VALUES (?, ?, ?)",
        [
            (1, 1, "2022-01-01"),  # студент 1 записался на курс 1
            (1, 2, "2022-02-01"),  # студент 1 записался на курс 2
            (1, 3, "2022-02-01"),  # студент 1 записался на курс 3
            (2, 2, "2022-02-01"),
            (2, 4, "2022-03-01"),
            (3, 3, "2022-03-01"),
            (3, 4, "2022-04-01"),
            (4, 4, "2022-04-01"),
            (4, 5, "2022-05-01"),
            (5, 5, "2022-05-01"),
            (5, 1, "2022-01-01"),
        ],
    )

    conn.commit()

    # выводим данные о студентах
    print("\nСтуденты:")
    cursor.execute("SELECT * FROM Students")
    for row in cursor.fetchall():
        print(row)

    conn.close()


def select_data():
    """
    Используя команду SELECT, извлеките данные из одной из таблиц
    (например, все записи из таблицы Students).
    Используйте команду WHERE, чтобы отфильтровать данные по определенному условию
    (например, извлеките студентов с определенным возрастом или из конкретного города).
    """
    conn = sqlite3.connect("SchoolDB.db")
    cursor = conn.cursor()

    # выводим данные о студентах
    print("\nСтуденты:")
    cursor.execute("SELECT * FROM Students")
    for row in cursor.fetchall():
        print(row)

    # выводим данные о студентах имя и возраст
    print("\nСтуденты (Имя, Возраст):")
    cursor.execute("SELECT Name, Age FROM Students")
    for row in cursor.fetchall():
        print(row)

    # выводим данные о студентах имя и возраст, где возраст больше 23
    print("\nСтуденты (Имя, Возраст > 23):")
    cursor.execute("SELECT * FROM Students WHERE Age > 23")
    for row in cursor.fetchall():
        print(row)

    # выводим данные о студентах имя, где имя равно David
    print("\nСтуденты (Имя = 'Charlie'):")
    cursor.execute("SELECT * FROM Students WHERE Name LIKE 'Charlie'")
    for row in cursor.fetchall():
        print(row)

    conn.close()


def update_data():
    """
    Используя команды UPDATE, обновите определенные записи в таблице (например, измените возраст студента).
    """
    conn = sqlite3.connect("SchoolDB.db")
    cursor = conn.cursor()

    # обновляем данные о Charlie (возраст 22)
    cursor.execute("UPDATE Students SET Age = 22 WHERE Name = 'Charlie'")
    conn.commit()

    # выводим данные о Charlie
    print("\nСтуденты ('Charlie', возраст 22):")
    cursor.execute("SELECT * FROM Students WHERE Name LIKE 'Charlie'")
    for row in cursor.fetchall():
        print(row)

    # обновляем данные о Charlie (возраст 21)
    cursor.execute("UPDATE Students SET Age = 21 WHERE Name = 'Charlie'")
    conn.commit()

    # выводим данные о Charlie
    print("\nСтуденты ('Charlie', возраст 21):")
    cursor.execute("SELECT * FROM Students WHERE Name LIKE 'Charlie'")
    for row in cursor.fetchall():
        print(row)

    conn.close()


def delete_data():
    """
    Используя команды DELETE, удалите ненужные записи.
    """
    conn = sqlite3.connect("SchoolDB.db")
    cursor = conn.cursor()

    # выводим данные о студентах
    print("\nСтуденты (с 'Charlie'):")
    cursor.execute("SELECT * FROM Students")
    for row in cursor.fetchall():
        print(row)

    # удаляем данные о Charlie
    cursor.execute("DELETE FROM Students WHERE Name = 'Charlie'")
    conn.commit()

    # выводим данные о студентах после удаления
    print("\nСтуденты (после удаления 'Charlie'):")
    cursor.execute("SELECT * FROM Students")
    for row in cursor.fetchall():
        print(row)

    # вставляем Charlie назад
    cursor.executemany(
        "INSERT INTO Students (Name, Age, Gender, EnrollmentDate) VALUES (?, ?, ?, ?)",
        [
            ("Charlie", 22, "Female", "2022-03-01"),
        ],
    )
    conn.commit()
    conn.close()


if __name__ == "__main__":
    create_tables()
    insert_sample_data()
    # select_data()
    # update_data()
    # delete_data()

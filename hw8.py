import sqlite3

conn = sqlite3.connect("geeks.db")
cursor = conn.cursor()


cursor.execute("""
                CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL
)
""")

cursor.execute("""
                CREATE TABLE IF NOT EXISTS courses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL
)   
""")

cursor.execute("""
                CREATE TABLE IF NOT EXISTS enrollments (
                student_id INTEGER,
                course_id INTEGER,
                grade INTEGER,
                FOREIGN KEY (student_id) REFERENCES students(id),
                FOREIGN KEY (course_id) REFERENCES courses(id)
)
""")

conn.commit()

class Student:
    def __init__(self, name):
        self.name = name

    def save(self):
        cursor.execute("INSERT INTO students (name) VALUES (?)", (self.name,))
        conn.commit()

    @staticmethod
    def enroll(student_id, course_id, grade):
        cursor.execute("INSERT INTO enrollments (student_id, course_id, grade) VALUES (?, ?, ?)", (student_id, course_id, grade))
        conn.commit()


class Course:
    def __init__(self, title):
        self.title = title

    def save(self):
        cursor.execute("INSERT INTO courses (title) VALUES (?)", (self.title,))
        conn.commit()



student1 = Student("Islam")
student1.save()
student2 = Student("Aslan")
student2.save()
student3 = Student("Asyl")
student3.save()

course1 = Course("Backend")
course1.save()
course2 = Course("Frontend")
course2.save()
course3 = Course("Desing")
course3.save()

cursor.execute("SELECT id FROM students")
student_ids = cursor.fetchall()
for row in student_ids:
    print(row[0])

cursor.execute("SELECT id FROM courses")
course_ids = cursor.fetchall()
for row in course_ids:
    print(row[0])

Student.enroll(student_ids[0][0], course_ids[0][0], 96)
Student.enroll(student_ids[1][0], course_ids[1][0], 92)
Student.enroll(student_ids[2][0], course_ids[2][0], 89)


cursor.execute("""
                SELECT students.name, courses.title
                FROM enrollments
                JOIN students ON enrollments.student_id = students.id
                JOIN courses ON enrollments.course_id = courses.id
""")
for row in cursor.fetchall():
    print(f"{row[0]} записан на курс: {row[1]}")


cursor.execute("""
            SELECT courses.title, AVG(enrollments.grade)
                FROM enrollments
                JOIN courses ON enrollments.course_id = courses.id
                GROUP BY courses.title
""")
for row in cursor.fetchall():
    print(f"{row[0]} средняя оценка: {int(row[1])}")

cursor.execute("""
            SELECT name FROM students
                WHERE id IN (
                SELECT student_id FROM enrollments WHERE grade > 90
)
""")
for row in cursor.fetchall():
    print(row[0])

cursor.execute("""
            SELECT title FROM courses
                WHERE id NOT IN (
                SELECT DISTINCT course_id FROM enrollments
)
""")
for row in cursor.fetchall():
    print(row[0])


cursor.execute("DROP VIEW IF EXISTS high_achievers")
cursor.execute("""
            CREATE VIEW high_achievers AS
                SELECT students.name AS student_name,
                courses.title AS course_title,
                enrollments.grade
            FROM enrollments
                JOIN students ON enrollments.student_id = students.id
                JOIN courses ON enrollments.course_id = courses.id
                WHERE enrollments.grade > 85
""")

cursor.execute("SELECT * FROM high_achievers")
for row in cursor.fetchall():
    print(row)

conn.commit()
conn.close()

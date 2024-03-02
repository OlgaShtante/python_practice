CREATE TABLE students (
    id SERIAL PRIMARY KEY,
    name VARCHAR NOT NULL,
    age INTEGER NOT NULL CHECK (age BETWEEN 6 AND 18)
);

CREATE TABLE subjects (
    id SERIAL PRIMARY KEY,
    name VARCHAR NOT NULL UNIQUE
);

CREATE TABLE teachers (
    id SERIAL PRIMARY KEY,
    name VARCHAR NOT NULL,
    subject_id INTEGER NOT NULL REFERENCES subjects(id)
);

CREATE TABLE grades (
    id SERIAL PRIMARY KEY,
    student_id INTEGER NOT NULL REFERENCES students(id),
    grade INTEGER NOT NULL CHECK (grade BETWEEN 1 AND 10),
    letter VARCHAR NOT NULL CHECK (letter BETWEEN 'a' AND 'z')
);

CREATE TABLE marks (
    id SERIAL PRIMARY KEY,
    student_id INTEGER NOT NULL REFERENCES students(id),
    subject_id INTEGER NOT NULL REFERENCES subjects(id),
    mark INTEGER NOT NULL
);

INSERT INTO students (name, age) VALUES
('Кира', 15),
('Иван', 16),
('Леонид', 17),
('Елена', 14),
('Анна', 13),
('Галина', 15),
('Виктор', 16),
('Борис', 16),
('Мария', 12),
('Лера', 12);

INSERT INTO subjects (name) VALUES
('Математика'),
('Физика'),
('Химия'),
('Биология'),
('История'),
('Английский язык'),
('Литература')

INSERT INTO teachers (name, subject_id) VALUES
('Иван Васильевич', 1),
('Александр Петрович', 2),
('Степан Валентинович', 3),
('Инна Аркадьевна', 4),
('Людмила Анатольевна', 5),
('Игорь Парфимович', 6),
('Дмитрий Валерьевич', 7);

INSERT INTO grades (student_id, grade, letter) VALUES
(1, 9, 'A'),
(2, 8, 'B'),
(3, 10, 'A'),
(4, 7, 'C'),
(5, 8, 'B'),
(6, 9, 'A'),
(7, 6, 'D'),
(8, 8, 'B'),
(9, 7, 'C'),
(10, 9, 'A');

INSERT INTO marks (student_id, subject_id, mark) VALUES
(1, 1, 10),
(2, 2, 8),
(3, 1, 9),
(4, 3, 8),
(5, 2, 9),
(6, 1, 7),
(7, 4, 5),
(8, 6, 6),
(9, 7, 10),
(10, 2, 7);

CREATE INDEX idx_students_name ON Students (name);
CREATE INDEX idx_teachers_name ON Teachers (name);
CREATE INDEX idx_subjects_name ON Subjects (name);
CREATE INDEX idx_grades_student_id ON Grades (id);
CREATE INDEX idx_grades_subject_id ON Grades (id);

SELECT name, age
FROM students
JOIN grades ON students.id = grades.student_id
where grades.grade = '10' AND grades.letter='A'

SELECT teachers.name, subjects.name
FROM teachers
JOIN subjects ON teachers.subject_id = subjects.id
WHERE subjects.name IN ('Математика', 'Физика');

SELECT students.name, AVG(marks.mark) AS average_rate
FROM students
JOIN marks ON students.id = marks.student_id
GROUP BY students.name;

SELECT students.name, MAX(marks.mark) AS best_mark
FROM students
JOIN marks ON students.id = marks.student_id
JOIN subjects ON marks.subject_id = subjects.id
WHERE subjects.name like '%Английский%'
GROUP BY students.name;

SELECT teachers.name, COUNT(*) AS num_subjects
FROM teachers
GROUP BY teachers.name
HAVING COUNT(*) > 1;

WITH studentGrade AS (
    SELECT grade
    FROM students
    JOIN grades ON students.id = grades.student_id
    WHERE students.name LIKE '%Анна%'
)
SELECT students.name AS student_name, CONCAT(grades.grade, grades.letter) AS grade
FROM students 
JOIN grades ON students.id = grades.student_id
JOIN studentGrade  ON studentGrade.grade = grades.grade;

SELECT CONCAT(grades.grade, grades.letter) AS grade, COUNT(*) AS num_students
FROM students
JOIN grades ON students.id = grades.student_id
GROUP BY grade, letter;

SELECT name
FROM subjects
WHERE id NOT IN (SELECT subject_id FROM marks);
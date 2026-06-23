-- Create the Database
CREATE DATABASE LibraryDB;
USE LibraryDB;

-- 1. Create Publisher Table
CREATE TABLE Publisher (
    Pub_id INT PRIMARY KEY,
    Name VARCHAR(100),
    Address VARCHAR(255)
);

-- 2. Create Member Table
CREATE TABLE Member (
    Memb_Id INT PRIMARY KEY,
    Name VARCHAR(100),
    Address VARCHAR(255),
    Memb_type VARCHAR(50),
    Memb_date DATE,
    Expiry_date DATE
);

-- 3. Create Books Table
CREATE TABLE Books (
    book_id INT PRIMARY KEY,
    Title VARCHAR(150),
    Author VARCHAR(100),
    Price DECIMAL(8,2),
    Available INT,
    Pub_id INT,
    FOREIGN KEY (Pub_id) REFERENCES Publisher(Pub_id)
);

-- 4. Create Borrow Table (Junction Table for the Many-to-Many relationship)
CREATE TABLE Borrow_Log (
    Issue_id INT PRIMARY KEY,
    book_id INT,
    Memb_Id INT,
    Issue_date DATE,
    Due_date DATE,
    Return_date DATE,
    FOREIGN KEY (book_id) REFERENCES Books(book_id),
    FOREIGN KEY (Memb_Id) REFERENCES Member(Memb_Id)
);


-- ==========================================
-- ADDING SAMPLE DATA (105 total rows)
-- ==========================================

-- Insert 10 Publishers
INSERT INTO Publisher VALUES (101, 'OReilly Media', 'USA');
INSERT INTO Publisher VALUES (102, 'Pearson Education', 'UK');
INSERT INTO Publisher VALUES (103, 'McGraw-Hill', 'USA');
INSERT INTO Publisher VALUES (104, 'MIT Press', 'USA');
INSERT INTO Publisher VALUES (105, 'Springer', 'Germany');
INSERT INTO Publisher VALUES (106, 'Oxford Press', 'UK');
INSERT INTO Publisher VALUES (107, 'Cambridge Press', 'UK');
INSERT INTO Publisher VALUES (108, 'HarperCollins', 'USA');
INSERT INTO Publisher VALUES (109, 'Penguin Books', 'UK');
INSERT INTO Publisher VALUES (110, 'Wiley', 'USA');

-- Insert 25 Books
INSERT INTO Books VALUES (201, 'Algorithms', 'Thomas Cormen', 1200, 5, 104);
INSERT INTO Books VALUES (202, 'Database Concepts', 'Abraham Silberschatz', 950, 4, 103);
INSERT INTO Books VALUES (203, 'Clean Code', 'Robert Martin', 800, 3, 102);
INSERT INTO Books VALUES (204, 'Data Applications', 'Martin Kleppmann', 1100, 6, 101);
INSERT INTO Books VALUES (205, 'Artificial Intelligence', 'Stuart Russell', 1500, 2, 102);
INSERT INTO Books VALUES (206, 'Pragmatic Programmer', 'Andrew Hunt', 850, 4, 102);
INSERT INTO Books VALUES (207, 'Computer Networking', 'James Kurose', 900, 5, 102);
INSERT INTO Books VALUES (208, 'Operating Systems', 'Abraham Silberschatz', 920, 3, 110);
INSERT INTO Books VALUES (209, 'Design Patterns', 'Erich Gamma', 750, 4, 102);
INSERT INTO Books VALUES (210, 'Compilers', 'Alfred Aho', 1300, 2, 102);
INSERT INTO Books VALUES (211, 'C Language', 'Brian Kernighan', 450, 7, 102);
INSERT INTO Books VALUES (212, 'Effective Java', 'Joshua Bloch', 700, 5, 102);
INSERT INTO Books VALUES (213, 'Head First Patterns', 'Eric Freeman', 650, 4, 101);
INSERT INTO Books VALUES (214, 'Code Complete', 'Steve McConnell', 950, 3, 103);
INSERT INTO Books VALUES (215, 'Python Crash Course', 'Eric Matthes', 550, 8, 110);
INSERT INTO Books VALUES (216, 'Mythical Man-Month', 'Fred Brooks', 400, 3, 102);
INSERT INTO Books VALUES (217, 'Refactoring', 'Martin Fowler', 850, 4, 102);
INSERT INTO Books VALUES (218, 'Theory of Computation', 'Michael Sipser', 1050, 3, 103);
INSERT INTO Books VALUES (219, 'SICP', 'Harold Abelson', 1250, 2, 104);
INSERT INTO Books VALUES (220, 'Deep Learning', 'Ian Goodfellow', 1400, 4, 104);
INSERT INTO Books VALUES (221, 'Data Science', 'Joel Grus', 600, 5, 101);
INSERT INTO Books VALUES (222, 'JavaScript Parts', 'Douglas Crockford', 350, 6, 101);
INSERT INTO Books VALUES (223, 'SQL Performance', 'Markus Winand', 500, 3, 105);
INSERT INTO Books VALUES (224, 'The Hobbit', 'J.R.R. Tolkien', 450, 10, 108);
INSERT INTO Books VALUES (225, '1984', 'George Orwell', 300, 12, 109);

-- Insert 20 Members
INSERT INTO Member VALUES (301, 'Sai Hrudai', 'Hyderabad', 'Student', '2026-01-10', '2027-01-10');
INSERT INTO Member VALUES (302, 'Amit Sharma', 'Delhi', 'Student', '2026-02-15', '2027-02-15');
INSERT INTO Member VALUES (303, 'Dr. John Doe', 'Boston', 'Faculty', '2026-06-01', '2029-06-01');
INSERT INTO Member VALUES (304, 'Priyal Patel', 'Mumbai', 'Student', '2026-03-20', '2027-03-20');
INSERT INTO Member VALUES (305, 'Rahul Verma', 'Bangalore', 'Student', '2026-01-15', '2027-01-15');
INSERT INTO Member VALUES (306, 'Prof. S. Rao', 'Chennai', 'Faculty', '2026-08-12', '2029-08-12');
INSERT INTO Member VALUES (307, 'Sneha Reddy', 'Hyderabad', 'Student', '2026-04-05', '2027-04-05');
INSERT INTO Member VALUES (308, 'Vikram Malhotra', 'Pune', 'Student', '2026-02-10', '2027-02-10');
INSERT INTO Member VALUES (309, 'Ananya Sen', 'Kolkata', 'Student', '2026-01-22', '2027-01-22');
INSERT INTO Member VALUES (310, 'David Miller', 'London', 'Student', '2026-03-01', '2027-03-01');
INSERT INTO Member VALUES (311, 'Sarah Jenkins', 'New York', 'Student', '2026-02-18', '2027-02-18');
INSERT INTO Member VALUES (312, 'James Wilson', 'Austin', 'Student', '2026-05-12', '2027-05-12');
INSERT INTO Member VALUES (313, 'Emily Brown', 'Chicago', 'Student', '2026-04-19', '2027-04-19');
INSERT INTO Member VALUES (314, 'Michael Chang', 'San Francisco', 'Student', '2026-01-30', '2027-01-30');
INSERT INTO Member VALUES (315, 'Dr. Lisa Ray', 'Toronto', 'Faculty', '2026-09-15', '2029-09-15');
INSERT INTO Member VALUES (316, 'Rohan Das', 'Kolkata', 'Student', '2026-03-25', '2027-03-25');
INSERT INTO Member VALUES (317, 'Nisha Gupta', 'Delhi', 'Student', '2026-02-28', '2027-02-28');
INSERT INTO Member VALUES (318, 'Karan Malhotra', 'Mumbai', 'Student', '2026-01-05', '2027-01-05');
INSERT INTO Member VALUES (319, 'Divya Nair', 'Kochi', 'Student', '2026-04-12', '2027-04-12');
INSERT INTO Member VALUES (320, 'Abhishek Jha', 'Patna', 'Student', '2026-05-01', '2027-05-01');

-- Insert 50 Borrow Records
INSERT INTO Borrow_Log VALUES (401, 201, 301, '2026-05-10', '2026-05-25', '2026-05-24');
INSERT INTO Borrow_Log VALUES (402, 202, 301, '2026-05-11', '2026-05-26', '2026-05-25');
INSERT INTO Borrow_Log VALUES (403, 203, 302, '2026-05-12', '2026-05-27', '2026-05-27');
INSERT INTO Borrow_Log VALUES (404, 204, 303, '2026-05-12', '2026-06-12', '2026-06-10');
INSERT INTO Borrow_Log VALUES (405, 205, 304, '2026-05-14', '2026-05-29', '2026-05-28');
INSERT INTO Borrow_Log VALUES (406, 206, 305, '2026-05-15', '2026-05-30', '2026-06-01');
INSERT INTO Borrow_Log VALUES (407, 207, 306, '2026-05-15', '2026-06-15', '2026-06-14');
INSERT INTO Borrow_Log VALUES (408, 208, 307, '2026-05-16', '2026-05-31', '2026-05-30');
INSERT INTO Borrow_Log VALUES (409, 209, 308, '2026-05-18', '2026-06-02', '2026-06-02');
INSERT INTO Borrow_Log VALUES (410, 210, 309, '2026-05-20', '2026-06-04', NULL);
INSERT INTO Borrow_Log VALUES (411, 211, 310, '2026-05-21', '2026-06-05', '2026-06-04');
INSERT INTO Borrow_Log VALUES (412, 212, 311, '2026-05-22', '2026-06-06', NULL);
INSERT INTO Borrow_Log VALUES (413, 213, 312, '2026-05-22', '2026-06-06', '2026-06-05');
INSERT INTO Borrow_Log VALUES (414, 214, 313, '2026-05-24', '2026-06-08', '2026-06-08');
INSERT INTO Borrow_Log VALUES (415, 215, 314, '2026-05-25', '2026-06-09', NULL);
INSERT INTO Borrow_Log VALUES (416, 216, 315, '2026-05-25', '2026-06-25', '2026-06-20');
INSERT INTO Borrow_Log VALUES (417, 217, 316, '2026-05-26', '2026-06-10', '2026-06-09');
INSERT INTO Borrow_Log VALUES (418, 218, 317, '2026-05-27', '2026-06-11', NULL);
INSERT INTO Borrow_Log VALUES (419, 219, 318, '2026-05-28', '2026-06-12', '2026-06-12');
INSERT INTO Borrow_Log VALUES (420, 220, 319, '2026-05-29', '2026-06-13', NULL);
INSERT INTO Borrow_Log VALUES (421, 221, 320, '2026-05-30', '2026-06-14', '2026-06-13');
INSERT INTO Borrow_Log VALUES (422, 222, 301, '2026-06-01', '2026-06-16', NULL);
INSERT INTO Borrow_Log VALUES (423, 223, 302, '2026-06-01', '2026-06-16', '2026-06-15');
INSERT INTO Borrow_Log VALUES (424, 224, 303, '2026-06-02', '2026-07-02', '2026-06-28');
INSERT INTO Borrow_Log VALUES (425, 225, 304, '2026-06-02', '2026-06-17', NULL);
INSERT INTO Borrow_Log VALUES (426, 201, 305, '2026-06-03', '2026-06-18', '2026-06-17');
INSERT INTO Borrow_Log VALUES (427, 202, 306, '2026-06-04', '2026-07-04', NULL);
INSERT INTO Borrow_Log VALUES (428, 203, 307, '2026-06-05', '2026-06-20', '2026-06-20');
INSERT INTO Borrow_Log VALUES (429, 204, 308, '2026-06-05', '2026-06-20', NULL);
INSERT INTO Borrow_Log VALUES (430, 205, 309, '2026-06-06', '2026-06-21', '2026-06-21');
INSERT INTO Borrow_Log VALUES (431, 206, 310, '2026-06-07', '2026-06-22', NULL);
INSERT INTO Borrow_Log VALUES (432, 207, 311, '2026-06-08', '2026-06-23', '2026-06-22');
INSERT INTO Borrow_Log VALUES (433, 208, 312, '2026-06-09', '2026-06-24', NULL);
INSERT INTO Borrow_Log VALUES (434, 209, 313, '2026-06-10', '2026-06-25', '2026-06-24');
INSERT INTO Borrow_Log VALUES (435, 210, 314, '2026-06-11', '2026-06-26', NULL);
INSERT INTO Borrow_Log VALUES (436, 211, 315, '2026-06-11', '2026-07-11', '2026-07-05');
INSERT INTO Borrow_Log VALUES (437, 212, 316, '2026-06-12', '2026-06-27', NULL);
INSERT INTO Borrow_Log VALUES (438, 213, 317, '2026-06-12', '2026-06-27', '2026-06-25');
INSERT INTO Borrow_Log VALUES (439, 214, 318, '2026-06-13', '2026-06-28', NULL);
INSERT INTO Borrow_Log VALUES (440, 215, 319, '2026-06-14', '2026-06-29', '2026-06-29');
INSERT INTO Borrow_Log VALUES (441, 216, 320, '2026-06-15', '2026-06-30', NULL);
INSERT INTO Borrow_Log VALUES (442, 217, 301, '2026-06-15', '2026-06-30', '2026-06-30');
INSERT INTO Borrow_Log VALUES (443, 218, 302, '2026-06-16', '2026-07-01', NULL);
INSERT INTO Borrow_Log VALUES (444, 219, 303, '2026-06-16', '2026-07-16', '2026-07-10');
INSERT INTO Borrow_Log VALUES (445, 220, 304, '2026-06-17', '2026-07-02', NULL);
INSERT INTO Borrow_Log VALUES (446, 221, 305, '2026-06-18', '2026-07-03', '2026-07-02');
INSERT INTO Borrow_Log VALUES (447, 222, 306, '2026-06-19', '2026-07-19', NULL);
INSERT INTO Borrow_Log VALUES (448, 223, 307, '2026-06-20', '2026-07-05', '2026-07-04');
INSERT INTO Borrow_Log VALUES (449, 224, 308, '2026-06-20', '2026-07-05', NULL);
INSERT INTO Borrow_Log VALUES (450, 225, 309, '2026-06-21', '2026-07-06', '2026-07-06');


-- ==========================================
-- THE 4 REQUIRED ADVANCED GRADED QUERIES
-- ==========================================

-- A. INNER JOIN: Combine data from tables to show who has what book
SELECT Member.Name, Books.Title, Borrow_Log.Issue_date
FROM Borrow_Log
INNER JOIN Member ON Borrow_Log.Memb_Id = Member.Memb_Id
INNER JOIN Books ON Borrow_Log.book_id = Books.book_id;

-- B. GROUP BY + HAVING: Count books borrowed per member, find who has more than 2
SELECT Member.Name, COUNT(Borrow_Log.Issue_id)
FROM Borrow_Log
INNER JOIN Member ON Borrow_Log.Memb_Id = Member.Memb_Id
GROUP BY Member.Name
HAVING COUNT(Borrow_Log.Issue_id) > 2;

-- C. SUBQUERY: Find books published by 'OReilly Media'
SELECT Title, Author FROM Books 
WHERE Pub_id = (SELECT Pub_id FROM Publisher WHERE Name = 'OReilly Media');

-- D. CREATE VIEW: A virtual helper table showing unreturned logs
CREATE VIEW ActiveLoans AS
SELECT Borrow_Log.Issue_id, Member.Name, Books.Title, Borrow_Log.Due_date
FROM Borrow_Log
INNER JOIN Member ON Borrow_Log.Memb_Id = Member.Memb_Id
INNER JOIN Books ON Borrow_Log.book_id = Books.book_id
WHERE Borrow_Log.Return_date IS NULL;

-- See the View data
SELECT * FROM ActiveLoans;
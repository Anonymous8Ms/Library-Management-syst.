from flask import Flask, render_template, request, jsonify, redirect, url_for
import sqlite3
import os
from datetime import date, datetime

app = Flask(__name__)
DB_PATH = os.path.join(os.path.dirname(__file__), 'LibraryDB.db')


def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def init_db():
    conn = get_db()
    cur = conn.cursor()

    cur.execute('''CREATE TABLE IF NOT EXISTS Publisher (
        Pub_id INTEGER PRIMARY KEY,
        Name TEXT,
        Address TEXT
    )''')

    cur.execute('''CREATE TABLE IF NOT EXISTS Member (
        Memb_Id INTEGER PRIMARY KEY,
        Name TEXT,
        Address TEXT,
        Memb_type TEXT,
        Memb_date TEXT,
        Expiry_date TEXT
    )''')

    cur.execute('''CREATE TABLE IF NOT EXISTS Books (
        book_id INTEGER PRIMARY KEY,
        Title TEXT,
        Author TEXT,
        Price REAL,
        Available INTEGER,
        Pub_id INTEGER,
        FOREIGN KEY (Pub_id) REFERENCES Publisher(Pub_id)
    )''')

    cur.execute('''CREATE TABLE IF NOT EXISTS Borrow_Log (
        Issue_id INTEGER PRIMARY KEY,
        book_id INTEGER,
        Memb_Id INTEGER,
        Issue_date TEXT,
        Due_date TEXT,
        Return_date TEXT,
        FOREIGN KEY (book_id) REFERENCES Books(book_id),
        FOREIGN KEY (Memb_Id) REFERENCES Member(Memb_Id)
    )''')

    cur.execute("SELECT COUNT(*) FROM Publisher")
    if cur.fetchone()[0] == 0:
        publishers = [
            (101, 'OReilly Media', 'USA'), (102, 'Pearson Education', 'UK'),
            (103, 'McGraw-Hill', 'USA'), (104, 'MIT Press', 'USA'),
            (105, 'Springer', 'Germany'), (106, 'Oxford Press', 'UK'),
            (107, 'Cambridge Press', 'UK'), (108, 'HarperCollins', 'USA'),
            (109, 'Penguin Books', 'UK'), (110, 'Wiley', 'USA')
        ]
        cur.executemany("INSERT INTO Publisher VALUES (?, ?, ?)", publishers)

        books = [
            (201, 'Algorithms', 'Thomas Cormen', 1200, 5, 104),
            (202, 'Database Concepts', 'Abraham Silberschatz', 950, 4, 103),
            (203, 'Clean Code', 'Robert Martin', 800, 3, 102),
            (204, 'Data Applications', 'Martin Kleppmann', 1100, 6, 101),
            (205, 'Artificial Intelligence', 'Stuart Russell', 1500, 2, 102),
            (206, 'Pragmatic Programmer', 'Andrew Hunt', 850, 4, 102),
            (207, 'Computer Networking', 'James Kurose', 900, 5, 102),
            (208, 'Operating Systems', 'Abraham Silberschatz', 920, 3, 110),
            (209, 'Design Patterns', 'Erich Gamma', 750, 4, 102),
            (210, 'Compilers', 'Alfred Aho', 1300, 2, 102),
            (211, 'C Language', 'Brian Kernighan', 450, 7, 102),
            (212, 'Effective Java', 'Joshua Bloch', 700, 5, 102),
            (213, 'Head First Patterns', 'Eric Freeman', 650, 4, 101),
            (214, 'Code Complete', 'Steve McConnell', 950, 3, 103),
            (215, 'Python Crash Course', 'Eric Matthes', 550, 8, 110),
            (216, 'Mythical Man-Month', 'Fred Brooks', 400, 3, 102),
            (217, 'Refactoring', 'Martin Fowler', 850, 4, 102),
            (218, 'Theory of Computation', 'Michael Sipser', 1050, 3, 103),
            (219, 'SICP', 'Harold Abelson', 1250, 2, 104),
            (220, 'Deep Learning', 'Ian Goodfellow', 1400, 4, 104),
            (221, 'Data Science', 'Joel Grus', 600, 5, 101),
            (222, 'JavaScript Parts', 'Douglas Crockford', 350, 6, 101),
            (223, 'SQL Performance', 'Markus Winand', 500, 3, 105),
            (224, 'The Hobbit', 'J.R.R. Tolkien', 450, 10, 108),
            (225, '1984', 'George Orwell', 300, 12, 109),
        ]
        cur.executemany("INSERT INTO Books VALUES (?, ?, ?, ?, ?, ?)", books)

        members = [
            (301, 'Sai Hrudai', 'Hyderabad', 'Student', '2026-01-10', '2027-01-10'),
            (302, 'Amit Sharma', 'Delhi', 'Student', '2026-02-15', '2027-02-15'),
            (303, 'Dr. John Doe', 'Boston', 'Faculty', '2026-06-01', '2029-06-01'),
            (304, 'Priyal Patel', 'Mumbai', 'Student', '2026-03-20', '2027-03-20'),
            (305, 'Rahul Verma', 'Bangalore', 'Student', '2026-01-15', '2027-01-15'),
            (306, 'Prof. S. Rao', 'Chennai', 'Faculty', '2026-08-12', '2029-08-12'),
            (307, 'Sneha Reddy', 'Hyderabad', 'Student', '2026-04-05', '2027-04-05'),
            (308, 'Vikram Malhotra', 'Pune', 'Student', '2026-02-10', '2027-02-10'),
            (309, 'Ananya Sen', 'Kolkata', 'Student', '2026-01-22', '2027-01-22'),
            (310, 'David Miller', 'London', 'Student', '2026-03-01', '2027-03-01'),
            (311, 'Sarah Jenkins', 'New York', 'Student', '2026-02-18', '2027-02-18'),
            (312, 'James Wilson', 'Austin', 'Student', '2026-05-12', '2027-05-12'),
            (313, 'Emily Brown', 'Chicago', 'Student', '2026-04-19', '2027-04-19'),
            (314, 'Michael Chang', 'San Francisco', 'Student', '2026-01-30', '2027-01-30'),
            (315, 'Dr. Lisa Ray', 'Toronto', 'Faculty', '2026-09-15', '2029-09-15'),
            (316, 'Rohan Das', 'Kolkata', 'Student', '2026-03-25', '2027-03-25'),
            (317, 'Nisha Gupta', 'Delhi', 'Student', '2026-02-28', '2027-02-28'),
            (318, 'Karan Malhotra', 'Mumbai', 'Student', '2026-01-05', '2027-01-05'),
            (319, 'Divya Nair', 'Kochi', 'Student', '2026-04-12', '2027-04-12'),
            (320, 'Abhishek Jha', 'Patna', 'Student', '2026-05-01', '2027-05-01'),
        ]
        cur.executemany("INSERT INTO Member VALUES (?, ?, ?, ?, ?, ?)", members)

        borrows = [
            (401, 201, 301, '2026-05-10', '2026-05-25', '2026-05-24'),
            (402, 202, 301, '2026-05-11', '2026-05-26', '2026-05-25'),
            (403, 203, 302, '2026-05-12', '2026-05-27', '2026-05-27'),
            (404, 204, 303, '2026-05-12', '2026-06-12', '2026-06-10'),
            (405, 205, 304, '2026-05-14', '2026-05-29', '2026-05-28'),
            (406, 206, 305, '2026-05-15', '2026-05-30', '2026-06-01'),
            (407, 207, 306, '2026-05-15', '2026-06-15', '2026-06-14'),
            (408, 208, 307, '2026-05-16', '2026-05-31', '2026-05-30'),
            (409, 209, 308, '2026-05-18', '2026-06-02', '2026-06-02'),
            (410, 210, 309, '2026-05-20', '2026-06-04', None),
            (411, 211, 310, '2026-05-21', '2026-06-05', '2026-06-04'),
            (412, 212, 311, '2026-05-22', '2026-06-06', None),
            (413, 213, 312, '2026-05-22', '2026-06-06', '2026-06-05'),
            (414, 214, 313, '2026-05-24', '2026-06-08', '2026-06-08'),
            (415, 215, 314, '2026-05-25', '2026-06-09', None),
            (416, 216, 315, '2026-05-25', '2026-06-25', '2026-06-20'),
            (417, 217, 316, '2026-05-26', '2026-06-10', '2026-06-09'),
            (418, 218, 317, '2026-05-27', '2026-06-11', None),
            (419, 219, 318, '2026-05-28', '2026-06-12', '2026-06-12'),
            (420, 220, 319, '2026-05-29', '2026-06-13', None),
            (421, 221, 320, '2026-05-30', '2026-06-14', '2026-06-13'),
            (422, 222, 301, '2026-06-01', '2026-06-16', None),
            (423, 223, 302, '2026-06-01', '2026-06-16', '2026-06-15'),
            (424, 224, 303, '2026-06-02', '2026-07-02', '2026-06-28'),
            (425, 225, 304, '2026-06-02', '2026-06-17', None),
            (426, 201, 305, '2026-06-03', '2026-06-18', '2026-06-17'),
            (427, 202, 306, '2026-06-04', '2026-07-04', None),
            (428, 203, 307, '2026-06-05', '2026-06-20', '2026-06-20'),
            (429, 204, 308, '2026-06-05', '2026-06-20', None),
            (430, 205, 309, '2026-06-06', '2026-06-21', '2026-06-21'),
            (431, 206, 310, '2026-06-07', '2026-06-22', None),
            (432, 207, 311, '2026-06-08', '2026-06-23', '2026-06-22'),
            (433, 208, 312, '2026-06-09', '2026-06-24', None),
            (434, 209, 313, '2026-06-10', '2026-06-25', '2026-06-24'),
            (435, 210, 314, '2026-06-11', '2026-06-26', None),
            (436, 211, 315, '2026-06-11', '2026-07-11', '2026-07-05'),
            (437, 212, 316, '2026-06-12', '2026-06-27', None),
            (438, 213, 317, '2026-06-12', '2026-06-27', '2026-06-25'),
            (439, 214, 318, '2026-06-13', '2026-06-28', None),
            (440, 215, 319, '2026-06-14', '2026-06-29', '2026-06-29'),
            (441, 216, 320, '2026-06-15', '2026-06-30', None),
            (442, 217, 301, '2026-06-15', '2026-06-30', '2026-06-30'),
            (443, 218, 302, '2026-06-16', '2026-07-01', None),
            (444, 219, 303, '2026-06-16', '2026-07-16', '2026-07-10'),
            (445, 220, 304, '2026-06-17', '2026-07-02', None),
            (446, 221, 305, '2026-06-18', '2026-07-03', '2026-07-02'),
            (447, 222, 306, '2026-06-19', '2026-07-19', None),
            (448, 223, 307, '2026-06-20', '2026-07-05', '2026-07-04'),
            (449, 224, 308, '2026-06-20', '2026-07-05', None),
            (450, 225, 309, '2026-06-21', '2026-07-06', '2026-07-06'),
        ]
        cur.executemany("INSERT INTO Borrow_Log VALUES (?, ?, ?, ?, ?, ?)", borrows)

    conn.commit()
    conn.close()


# ─── PAGES ─────────────────────────────────────────────

@app.route('/')
def index():
    conn = get_db()
    c = conn.cursor()
    c.execute("SELECT COUNT(*) FROM Books")
    total_books = c.fetchone()[0]
    c.execute("SELECT COUNT(*) FROM Member")
    total_members = c.fetchone()[0]
    c.execute("SELECT COUNT(*) FROM Borrow_Log WHERE Return_date IS NULL")
    active_borrows = c.fetchone()[0]
    c.execute("SELECT COUNT(*) FROM Publisher")
    total_publishers = c.fetchone()[0]
    c.execute("SELECT COUNT(*) FROM Borrow_Log")
    total_borrows = c.fetchone()[0]
    conn.close()
    return render_template('index.html',
                           total_books=total_books,
                           total_members=total_members,
                           active_borrows=active_borrows,
                           total_publishers=total_publishers,
                           total_borrows=total_borrows)


@app.route('/books')
def books_page():
    conn = get_db()
    c = conn.cursor()
    c.execute("SELECT b.*, p.Name as Pub_name FROM Books b LEFT JOIN Publisher p ON b.Pub_id = p.Pub_id ORDER BY b.book_id")
    books = [dict(row) for row in c.fetchall()]
    c.execute("SELECT Pub_id, Name FROM Publisher ORDER BY Name")
    publishers = [dict(row) for row in c.fetchall()]
    conn.close()
    return render_template('books.html', books=books, publishers=publishers)


@app.route('/members')
def members_page():
    conn = get_db()
    c = conn.cursor()
    c.execute("SELECT * FROM Member ORDER BY Memb_Id")
    members = [dict(row) for row in c.fetchall()]
    conn.close()
    return render_template('members.html', members=members)


@app.route('/publishers')
def publishers_page():
    conn = get_db()
    c = conn.cursor()
    c.execute("SELECT * FROM Publisher ORDER BY Pub_id")
    publishers = [dict(row) for row in c.fetchall()]
    conn.close()
    return render_template('publishers.html', publishers=publishers)


@app.route('/borrows')
def borrows_page():
    conn = get_db()
    c = conn.cursor()
    c.execute('''SELECT bl.*, b.Title as Book_title, m.Name as Member_name
                 FROM Borrow_Log bl
                 LEFT JOIN Books b ON bl.book_id = b.book_id
                 LEFT JOIN Member m ON bl.Memb_Id = m.Memb_Id
                 ORDER BY bl.Issue_id''')
    borrows = [dict(row) for row in c.fetchall()]
    c.execute("SELECT book_id, Title FROM Books ORDER BY Title")
    books = [dict(row) for row in c.fetchall()]
    c.execute("SELECT Memb_Id, Name FROM Member ORDER BY Name")
    members = [dict(row) for row in c.fetchall()]
    conn.close()
    return render_template('borrows.html', borrows=borrows, books=books, members=members)


@app.route('/queries')
def queries_page():
    return render_template('queries.html')


# ─── API ROUTES ────────────────────────────────────────

@app.route('/api/books', methods=['POST'])
def add_book():
    data = request.json
    conn = get_db()
    conn.execute("INSERT INTO Books VALUES (?, ?, ?, ?, ?, ?)",
                 (data['book_id'], data['Title'], data['Author'],
                  data['Price'], data['Available'], data['Pub_id']))
    conn.commit()
    conn.close()
    return jsonify({'status': 'ok'})


@app.route('/api/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    conn = get_db()
    conn.execute("DELETE FROM Borrow_Log WHERE book_id = ?", (book_id,))
    conn.execute("DELETE FROM Books WHERE book_id = ?", (book_id,))
    conn.commit()
    conn.close()
    return jsonify({'status': 'ok'})


@app.route('/api/members', methods=['POST'])
def add_member():
    data = request.json
    conn = get_db()
    conn.execute("INSERT INTO Member VALUES (?, ?, ?, ?, ?, ?)",
                 (data['Memb_Id'], data['Name'], data['Address'],
                  data['Memb_type'], data['Memb_date'], data['Expiry_date']))
    conn.commit()
    conn.close()
    return jsonify({'status': 'ok'})


@app.route('/api/members/<int:memb_id>', methods=['DELETE'])
def delete_member(memb_id):
    conn = get_db()
    conn.execute("DELETE FROM Borrow_Log WHERE Memb_Id = ?", (memb_id,))
    conn.execute("DELETE FROM Member WHERE Memb_Id = ?", (memb_id,))
    conn.commit()
    conn.close()
    return jsonify({'status': 'ok'})


@app.route('/api/publishers', methods=['POST'])
def add_publisher():
    data = request.json
    conn = get_db()
    conn.execute("INSERT INTO Publisher VALUES (?, ?, ?)",
                 (data['Pub_id'], data['Name'], data['Address']))
    conn.commit()
    conn.close()
    return jsonify({'status': 'ok'})


@app.route('/api/publishers/<int:pub_id>', methods=['DELETE'])
def delete_publisher(pub_id):
    conn = get_db()
    conn.execute("DELETE FROM Books WHERE Pub_id = ?", (pub_id,))
    conn.execute("DELETE FROM Publisher WHERE Pub_id = ?", (pub_id,))
    conn.commit()
    conn.close()
    return jsonify({'status': 'ok'})


@app.route('/api/borrows', methods=['POST'])
def add_borrow():
    data = request.json
    conn = get_db()
    conn.execute("INSERT INTO Borrow_Log VALUES (?, ?, ?, ?, ?, ?)",
                 (data['Issue_id'], data['book_id'], data['Memb_Id'],
                  data['Issue_date'], data['Due_date'], None))
    conn.execute("UPDATE Books SET Available = Available - 1 WHERE book_id = ?", (data['book_id'],))
    conn.commit()
    conn.close()
    return jsonify({'status': 'ok'})


@app.route('/api/borrows/<int:issue_id>/return', methods=['POST'])
def return_book(issue_id):
    conn = get_db()
    c = conn.cursor()
    c.execute("SELECT book_id FROM Borrow_Log WHERE Issue_id = ?", (issue_id,))
    row = c.fetchone()
    if row:
        conn.execute("UPDATE Borrow_Log SET Return_date = ? WHERE Issue_id = ?",
                     (date.today().isoformat(), issue_id))
        conn.execute("UPDATE Books SET Available = Available + 1 WHERE book_id = ?", (row[0],))
        conn.commit()
    conn.close()
    return jsonify({'status': 'ok'})


@app.route('/api/borrows/<int:issue_id>', methods=['DELETE'])
def delete_borrow(issue_id):
    conn = get_db()
    c = conn.cursor()
    c.execute("SELECT book_id, Return_date FROM Borrow_Log WHERE Issue_id = ?", (issue_id,))
    row = c.fetchone()
    if row and row[1] is None:
        conn.execute("UPDATE Books SET Available = Available + 1 WHERE book_id = ?", (row[0],))
    conn.execute("DELETE FROM Borrow_Log WHERE Issue_id = ?", (issue_id,))
    conn.commit()
    conn.close()
    return jsonify({'status': 'ok'})


@app.route('/api/query/<int:q>')
def run_query(q):
    conn = get_db()
    c = conn.cursor()

    if q == 1:
        c.execute('''SELECT Member.Name, Books.Title, Borrow_Log.Issue_date
                     FROM Borrow_Log
                     INNER JOIN Member ON Borrow_Log.Memb_Id = Member.Memb_Id
                     INNER JOIN Books ON Borrow_Log.book_id = Books.book_id''')
    elif q == 2:
        c.execute('''SELECT Member.Name, COUNT(Borrow_Log.Issue_id) as borrow_count
                     FROM Borrow_Log
                     INNER JOIN Member ON Borrow_Log.Memb_Id = Member.Memb_Id
                     GROUP BY Member.Name
                     HAVING COUNT(Borrow_Log.Issue_id) > 2''')
    elif q == 3:
        c.execute('''SELECT Title, Author FROM Books
                     WHERE Pub_id = (SELECT Pub_id FROM Publisher WHERE Name = 'OReilly Media')''')
    elif q == 4:
        c.execute('''SELECT Borrow_Log.Issue_id, Member.Name, Books.Title, Borrow_Log.Due_date
                     FROM Borrow_Log
                     INNER JOIN Member ON Borrow_Log.Memb_Id = Member.Memb_Id
                     INNER JOIN Books ON Borrow_Log.book_id = Books.book_id
                     WHERE Borrow_Log.Return_date IS NULL''')

    columns = [desc[0] for desc in c.description]
    rows = [dict(zip(columns, row)) for row in c.fetchall()]
    conn.close()
    return jsonify({'columns': columns, 'rows': rows})


if __name__ == '__main__':
    init_db()
    app.run(debug=True, port=8080)

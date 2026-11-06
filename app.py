
from flask import Flask, render_template, request
import mysql.connector
import model
import sentiment

app = Flask(__name__)

# DATABASE CONNECTION
db = mysql.connector.connect(
    host="localhost",
    user="",
    password="",
    database="smartcampus"
)

cursor = db.cursor(buffered=True)


# HOME PAGE
@app.route('/')
def home():
    return render_template("index.html")

# FACULTY PROFILE
@app.route('/faculty_profile/<username>')
def faculty_profile(username):

    cursor.execute(
        "SELECT name, department, email, phone, subject FROM faculty WHERE username=%s",
        (username,)
    )

    data = cursor.fetchone()

    if not data:
        return "Faculty not found"

    faculty_data = {
    "username": username,   # ADD THIS
    "name": data[0],
    "department": data[1],
    "email": data[2],
    "phone": data[3],
    "subject": data[4]
}
    return render_template("faculty_profile.html", faculty=faculty_data)

# STUDENT PROFILE
@app.route('/student_profile/<username>')
def student_profile(username):

    cursor.execute(
        """
        SELECT name, attendance, dbms, python, ai
        FROM students
        WHERE username=%s
        """,
        (username,)
    )

    data = cursor.fetchone()

    if not data:
        return "Student not found"

    student_data = {
        "username": username,
        "name": data[0],
        "attendance": data[1],
        "dbms": data[2],
        "python": data[3],
        "ai": data[4]
    }

    return render_template(
        "student_profile.html",
        student=student_data
    )

# LOGIN
@app.route('/login', methods=['POST'])
def login():

    username = request.form['username']
    password = request.form['password']

    cursor.execute(
        "SELECT role FROM users WHERE username=%s AND password=%s",
        (username, password)
    )

    user = cursor.fetchone()

    if not user:
        return "Invalid Login"

    role = user[0]

    # STUDENT
    if role == "student":

        cursor.execute(
            "SELECT name, attendance, dbms, python, ai FROM students WHERE username=%s",
            (username,)
        )

        data = cursor.fetchone()

        name = data[0]
        attendance = int(data[1] or 0)
        dbms = int(data[2] or 0)
        python_marks = int(data[3] or 0)
        ai = int(data[4] or 0)

        percentage = round((dbms + python_marks + ai) / 3, 2)

        risk = model.predict_failure(attendance, percentage)
        placement = model.placement_score(percentage, attendance)
        suggestion = model.study_suggestion(percentage, attendance)

        return render_template(
    "student_dashboard.html",
    name=name,
    username=username,
    attendance=attendance,
    dbms=dbms,
    python=python_marks,
    ai=ai,
    percentage=percentage,
    risk=risk,
    placement=placement,
    suggestion=suggestion
)
    # FACULTY
    elif role == "faculty":

        cursor.execute("SELECT id, name FROM students")
        students = cursor.fetchall()

        return render_template(
            "faculty_dashboard.html",
            students=students,
            username=username,
        )

    # ADMIN
    else:

        cursor.execute("SELECT id, name FROM students")
        students = cursor.fetchall()

        return render_template(
            "admin_dashboard.html",
            students=students,
            student_data=None,
            feedbacks=[]
        )

# ADMIN VIEW STUDENT
@app.route('/admin_student', methods=['POST'])
def admin_student():

    student_id = request.form['student_id']

    cursor.execute(
        "SELECT name, attendance, dbms, python, ai FROM students WHERE id=%s",
        (student_id,)
    )

    data = cursor.fetchone()

    name = data[0]
    attendance = int(data[1] or 0)
    dbms = int(data[2] or 0)
    python_marks = int(data[3] or 0)
    ai = int(data[4] or 0)

    percentage = round((dbms + python_marks + ai) / 3, 2)

    student_data = {
        "name": name,
        "attendance": attendance,
        "dbms": dbms,
        "python": python_marks,
        "ai": ai,
        "percentage": percentage
    }

    # Fetch only that student's feedback
    cursor.execute(
        "SELECT feedback_text, sentiment FROM feedback WHERE student_id=%s",
        (student_id,)
    )

    feedbacks = cursor.fetchall()

    cursor.execute("SELECT id, name FROM students")
    students = cursor.fetchall()

    return render_template(
        "admin_dashboard.html",
        students=students,
        student_data=student_data,
        feedbacks=feedbacks
    )


# UPDATE STUDENT
@app.route('/update_student', methods=['POST'])
def update_student():

    student_id = request.form['student_id']
    dbms = request.form['dbms']
    python_marks = request.form['python']
    ai = request.form['ai']
    attendance = request.form['attendance']

    dbms = int(dbms or 0)
    python_marks = int(python_marks or 0)
    ai = int(ai or 0)
    attendance = int(attendance or 0)

    overall = round((dbms + python_marks + ai) / 3, 2)

    cursor.execute(
        "UPDATE students SET dbms=%s, python=%s, ai=%s, marks=%s, attendance=%s WHERE id=%s",
        (dbms, python_marks, ai, overall, attendance, student_id)
    )

    db.commit()

    return "Student Updated Successfully"


# FEEDBACK
@app.route('/feedback', methods=['POST'])
def feedback():

    text = request.form['feedback']
    username = request.form['username']

    cursor.execute(
        "SELECT id FROM students WHERE username=%s",
        (username,)
    )

    student = cursor.fetchone()
    student_id = student[0]

    result = sentiment.analyze_feedback(text)

    cursor.execute(
        "INSERT INTO feedback (feedback_text, sentiment, student_id) VALUES (%s,%s,%s)",
        (text, result, student_id)
    )

    db.commit()

    return "Feedback Sentiment : " + result

# UPDATE FACULTY PROFILE
@app.route('/update_faculty', methods=['POST'])
def update_faculty():

    username = request.form['username']
    name = request.form['name']
    department = request.form['department']
    email = request.form['email']
    phone = request.form['phone']
    subject = request.form['subject']

    cursor.execute(
        "UPDATE faculty SET name=%s, department=%s, email=%s, phone=%s, subject=%s WHERE username=%s",
        (name, department, email, phone, subject, username)
    )

    db.commit()

    return "Profile Updated Successfully"

@app.route('/update_student_profile', methods=['POST'])
def update_student_profile():

    username = request.form['username']
    name = request.form['name']

    cursor.execute(
        """
        UPDATE students
        SET name=%s
        WHERE username=%s
        """,
        (name, username)
    )

    db.commit()

    return "Profile Updated Successfully"

# LOGOUT
@app.route('/logout')
def logout():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)



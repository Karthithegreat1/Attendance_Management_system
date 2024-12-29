from flask import Flask, request, render_template
from flask_mysqldb import MySQL
from flask_mail import Mail, Message
from datetime import datetime

app = Flask(__name__)

# Configure MySQL
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'  # Replace with your MySQL username
app.config['MYSQL_PASSWORD'] = 'Karthick.2002'  # Replace with your MySQL password
app.config['MYSQL_DB'] = 'attendance_db'

mysql = MySQL(app)

# Configure Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'manokarthick.ks741@gmail.com'  # Replace with your email
app.config['MAIL_PASSWORD'] = 'zldx bawd gcln jqlw'  # Replace with your app password

mail = Mail(app)

@app.route('/')
def index():
    # Fetch students for attendance form
    cur = mysql.connection.cursor()
    cur.execute("SELECT StudentID, Name FROM Students")
    students = cur.fetchall()
    cur.close()
    return render_template('index.html', students=students)

@app.route('/mark_attendance', methods=['POST'])
def mark_attendance():
    student_id = request.form['StudentID']
    subject = request.form['Subject']
    teacher = request.form['Teacher']
    status = request.form['Status']
    date = datetime.now().strftime("%Y-%m-%d")

    # Save attendance in the database
    cur = mysql.connection.cursor()
    cur.execute("""
        INSERT INTO Attendance (StudentID, Date, Status, Subject, Teacher)
        VALUES (%s, %s, %s, %s, %s)
    """, (student_id, date, status, subject, teacher))
    mysql.connection.commit()

    # Fetch student email if marked absent
    if status.lower() == 'absent':
        cur.execute("SELECT Name, Email FROM Students WHERE StudentID = %s", (student_id,))
        student = cur.fetchone()
        if student:
            student_name, student_email = student
            # Send email notification
            msg = Message(
                subject="Attendance Notification",
                sender=app.config['MAIL_USERNAME'],
                recipients=[student_email],
                body=f"Dear {student_name},\n\nYou were marked as ABSENT for {subject} on {date} by {teacher}.\n\nBest regards,\nAttendance Management System"
            )
            mail.send(msg)

    cur.close()
    return render_template('success.html', message="Attendance marked and notifications sent successfully!")

if __name__ == '__main__':
    app.run(debug=True)

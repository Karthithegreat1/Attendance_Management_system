-- Create the database
CREATE DATABASE IF NOT EXISTS attendance_db;

-- Use the database
USE attendance_db;

-- Create the Students table
CREATE TABLE IF NOT EXISTS Students (
    StudentID INT PRIMARY KEY AUTO_INCREMENT,
    Name VARCHAR(100) NOT NULL,
    Email VARCHAR(100) NOT NULL UNIQUE,
    Course VARCHAR(100) NOT NULL
);

-- Create the Attendance table
CREATE TABLE IF NOT EXISTS Attendance (
    AttendanceID INT PRIMARY KEY AUTO_INCREMENT,
    StudentID INT NOT NULL,
    Date DATE NOT NULL,
    Status ENUM('Present', 'Absent') NOT NULL,
    Subject VARCHAR(100) NOT NULL,
    Teacher VARCHAR(100) NOT NULL,
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID)
);

-- Insert sample data into Students table
INSERT INTO Students (Name, Email, Course) VALUES
('Student1', 'karthik.m@mactores.in', 'Computer Science'),
('Jane Smith', 'jane.smith@example.com', 'Mathematics');

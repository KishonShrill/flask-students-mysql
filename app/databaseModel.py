from app import mysql

class DatabaseManager(object):


    def __init__(self, id=None, firstname=None, lastname=None, course=None, year=None, gender=None):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.course = course
        self.year = year
        self.gender = gender

    def add(self):
        try:
            cursor = mysql.connection.cursor()
            sql = """INSERT INTO students (id, firstname, lastname, course, year, gender)
                     VALUES (%s, %s, %s, %s, %s, %s)"""
            cursor.execute(sql, (self.id, self.firstname, self.lastname, self.course, self.year, self.gender))
            mysql.connection.commit()
        except Exception as e:
            print(f"Error adding student: {e}")
            mysql.connection.rollback()

    """ UPDATE METHOD """
    @classmethod
    def editStudent(cls, oldID, newFirstName, newLastName, newID, newYear, newGender, newCourse):
        try:
            cursor = mysql.connection.cursor()
            cursor.execute("""
                UPDATE student 
                SET FirstName = %s, LastName = %s, ID = %s, YearLevel = %s, Gender = %s, CourseCode = %s
                WHERE ID = %s
            """, (newFirstName, newLastName, newID, newYear, newGender, newCourse, oldID))
            mysql.connection.commit()
            return True
        except Exception as e:
            print(f"Error updating student: {e}")
            mysql.connection.rollback()
            return False
        
    
    
    """ DELETE METHOD """
    """ DELETE METHOD """
    """ DELETE METHOD """

    @classmethod
    def deleteStudent(cls, student_id):
        try:
            cursor = mysql.connection.cursor()
            sql = "DELETE FROM student WHERE ID = %s"
            cursor.execute(sql, (student_id,))
            mysql.connection.commit()
            return True
        except Exception as e:
            print(f"Error deleting student: {e}")
            mysql.connection.rollback()
            return False



    """ LIST METHOD """
    """ LIST METHOD """
    """ LIST METHOD """
    
    @classmethod
    def allStudents(cls):
        cursor = mysql.connection.cursor()

        sql = "SELECT * from student"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result
    
    @classmethod
    def allCourses(cls):
        cursor = mysql.connection.cursor()

        sql = "SELECT * from course ORDER BY course.CourseName ASC"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result
    
    @classmethod
    def allColleges(cls):
        cursor = mysql.connection.cursor()

        sql = "SELECT * from college"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result
    

    """ WEBSITE THINGS """
    """ WEBSITE THINGS """
    """ WEBSITE THINGS """

    @classmethod
    def queryStudentFirstNameWithCollege(cls, args: str, college: str):
        cursor = mysql.connection.cursor()
        cursor.execute("""
            SELECT *
            FROM student
            WHERE student.FirstName LIKE %s AND student.CourseCode = %s
        """, ('%' + args + '%', college))
        result = cursor.fetchall()
        return result
    
    @classmethod
    def queryStudentLastNameWithCollege(cls, args: str, college: str):
        cursor = mysql.connection.cursor()
        cursor.execute("""
            SELECT *
            FROM student
            WHERE student.LastName LIKE %s AND student.CourseCode = %s
        """, ('%' + args + '%', college))
        result = cursor.fetchall()
        return result
    
    @classmethod
    def queryStudentIDWithCollege(cls, args: str, college: str):
        cursor = mysql.connection.cursor()
        cursor.execute("""
            SELECT *
            FROM student
            WHERE student.ID LIKE %s AND student.CourseCode = %s
        """, ('%' + args + '%', college))
        result = cursor.fetchall()
        return result
    
    @classmethod
    def queryStudentYearWithCollege(cls, args: str, college: str):
        cursor = mysql.connection.cursor()
        cursor.execute("""
            SELECT *
            FROM student
            WHERE student.YearLevel LIKE %s AND student.CourseCode = %s
        """, ('%' + args + '%', college))
        result = cursor.fetchall()
        return result
    
    @classmethod
    def queryStudentGenderWithCollege(cls, args: str, college: str):
        cursor = mysql.connection.cursor()
        cursor.execute("""
            SELECT *
            FROM student
            WHERE student.Gender LIKE %s AND student.CourseCode = %s
        """, ('%' + args + '%', college))
        result = cursor.fetchall()
        return result
    
    @classmethod
    def queryStudentFirstName(cls, args: str):
        cursor = mysql.connection.cursor()
        cursor.execute("""
            SELECT *
            FROM student
            WHERE student.FirstName LIKE %s
        """, ('%' + args + '%',))
        result = cursor.fetchall()
        return result
    
    @classmethod
    def queryStudentLastName(cls, args: str):
        cursor = mysql.connection.cursor()
        cursor.execute("""
            SELECT *
            FROM student
            WHERE student.LastName LIKE %s
        """, ('%' + args + '%',))
        result = cursor.fetchall()
        return result
    
    @classmethod
    def queryStudentID(cls, args: str):
        cursor = mysql.connection.cursor()
        cursor.execute("""
            SELECT *
            FROM student
            WHERE student.ID LIKE %s
        """, ('%' + args + '%',))
        result = cursor.fetchall()
        return result
    
    @classmethod
    def queryStudentYear(cls, args: str):
        cursor = mysql.connection.cursor()
        cursor.execute("""
            SELECT *
            FROM student
            WHERE student.YearLevel LIKE %s
        """, ('%' + args + '%',))
        result = cursor.fetchall()
        return result
    
    @classmethod
    def queryStudentGender(cls, args: str):
        cursor = mysql.connection.cursor()
        cursor.execute("""
            SELECT *
            FROM student
            WHERE student.Gender LIKE %s
        """, ('%' + args + '%',))
        result = cursor.fetchall()
        return result
    
    @classmethod
    def queryCollege(cls, args: str):
        cursor = mysql.connection.cursor()
        cursor.execute("""
            SELECT *
            FROM student
            WHERE student.coursecode = %s
        """, (args,))
        result = cursor.fetchall()
        return result
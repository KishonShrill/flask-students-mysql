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
        cursor = mysql.connection.cursor()

        sql = f"INSERT INTO students(id, firstname, lastname, course, year, gender) \
                VALUES('{self.id}','{self.firstname}','{self.lastname}','{self.course}','{self.year}','{self.gender}')"
        
        cursor.execute(sql)
        mysql.connection.commit()

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
    def allColleges(cls):
        cursor = mysql.connection.cursor()

        sql = "SELECT * from college"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result
    
    @classmethod
    def allCourses(cls):
        cursor = mysql.connection.cursor()

        sql = "SELECT * from course"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result
    
    """ DELETE METHOD """
    """ DELETE METHOD """
    """ DELETE METHOD """

    @classmethod
    def deleteStudent(cls,id):
        try:
            cursor = mysql.connection.cursor()
            sql = f"DELETE from users where id= {id}"
            cursor.execute(sql)
            mysql.connection.commit()
            return True
        except:
            return False
from app import mysql

class Students(object):


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

    
    @classmethod
    def all(cls):
        cursor = mysql.connection.cursor()

        sql = "SELECT * from student"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result
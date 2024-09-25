from app import mysql

class DatabaseManager(object):


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


    """ CREATE METHOD """
    @classmethod
    def createStudent(cls, newFirstName, newLastName, newID, newYear, newGender, newCourse: str):
        try:
            cursor = mysql.connection.cursor()

            # If newCourse is None, set it to NULL in the query
            if newCourse == "None":
                query = """
                    INSERT INTO student(firstname, lastname, id, yearlevel, gender, coursecode) VALUE
                    (%s, %s, %s, %s, %s, NULL);
                """
                values = (newFirstName, newLastName, newID, newYear, newGender)
            else:
                query = """
                    INSERT INTO student(firstname, lastname, id, yearlevel, gender, coursecode) VALUE
                    (%s, %s, %s, %s, %s, %s);
                """
                values = (newFirstName, newLastName, newID, newYear, newGender, newCourse)

            cursor.execute(query, values)
            mysql.connection.commit()
            return True

        except Exception as e:
            print(f"Error creating student: {e}")
            mysql.connection.rollback()
            return False

    @classmethod
    def createProgram(cls, newName, newCode, newCollege):
        try:
            cursor = mysql.connection.cursor()
            cursor.execute("""
                INSERT INTO course(coursename, coursecode, collegecode) VALUE
                (%s, %s, %s);
            """, (newName, newCode, newCollege))
            mysql.connection.commit()
            return True
        
        except Exception as e:
            print(f"Error creating course: {e}")
            mysql.connection.rollback()
            return False


    """ UPDATE METHOD """    
    @classmethod
    def editStudent(cls, oldID, newFirstName, newLastName, newID, newYear, newGender, newCourse: str):
        try:
            cursor = mysql.connection.cursor()

            # If newCourse is None, set it to NULL in the query
            if newCourse == "None":
                query = """
                    UPDATE student 
                    SET FirstName = %s, LastName = %s, ID = %s, YearLevel = %s, Gender = %s, CourseCode = NULL
                    WHERE ID = %s
                """
                values = (newFirstName, newLastName, newID, newYear, newGender, oldID)
            else:
                query = """
                    UPDATE student 
                    SET FirstName = %s, LastName = %s, ID = %s, YearLevel = %s, Gender = %s, CourseCode = %s
                    WHERE ID = %s
                """
                values = (newFirstName, newLastName, newID, newYear, newGender, newCourse, oldID)

            cursor.execute(query, values)
            mysql.connection.commit()
            return True

        except Exception as e:
            print(f"Error updating student: {e}")
            mysql.connection.rollback()
            return False
        
    @classmethod
    def editProgram(cls, oldID, newName, newCode, newCollege):
        try:
            cursor = mysql.connection.cursor()
            cursor.execute("""
                UPDATE course
                SET CourseName = %s, CourseCode = %s, CollegeCode = %s
                WHERE CourseCode = %s
            """, (newName, newCode, newCollege, oldID))
            mysql.connection.commit()
            return True
        
        except Exception as e:
            print(f"Error updating course: {e}")
            mysql.connection.rollback()
            return False

    """ DELETE METHOD """
    """ DELETE METHOD """
    """ DELETE METHOD """

    @classmethod
    def deleteStudent(cls, student_id: str):
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
        
    @classmethod
    def deleteProgram(cls, course_id: str):
        try:
            cursor = mysql.connection.cursor()
            sql = "DELETE FROM course WHERE CourseCode = %s"
            cursor.execute(sql, (course_id,))
            mysql.connection.commit()
            return True
        except Exception as e:
            print(f"Error deleting program: {e}")
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
    def queryStudentFirstNameWithCourse(cls, args: str, college: str):
        cursor = mysql.connection.cursor()
        cursor.execute("""
            SELECT *
            FROM student
            WHERE student.FirstName LIKE %s AND student.CourseCode = %s
        """, ('%' + args + '%', college))
        result = cursor.fetchall()
        return result
    
    @classmethod
    def queryStudentLastNameWithCourse(cls, args: str, college: str):
        cursor = mysql.connection.cursor()
        cursor.execute("""
            SELECT *
            FROM student
            WHERE student.LastName LIKE %s AND student.CourseCode = %s
        """, ('%' + args + '%', college))
        result = cursor.fetchall()
        return result
    
    @classmethod
    def queryStudentIDWithCourse(cls, args: str, college: str):
        cursor = mysql.connection.cursor()
        cursor.execute("""
            SELECT *
            FROM student
            WHERE student.ID LIKE %s AND student.CourseCode = %s
        """, ('%' + args + '%', college))
        result = cursor.fetchall()
        return result
    
    @classmethod
    def queryStudentYearWithCourse(cls, args: str, college: str):
        cursor = mysql.connection.cursor()
        cursor.execute("""
            SELECT *
            FROM student
            WHERE student.YearLevel LIKE %s AND student.CourseCode = %s
        """, ('%' + args + '%', college))
        result = cursor.fetchall()
        return result
    
    @classmethod
    def queryStudentGenderWithCourse(cls, args: str, college: str):
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
    # def queryStudentID(cls, args: str):
    def queryStudentWithID(cls, args: str):
        cursor = mysql.connection.cursor()
        query = """
            SELECT *
            FROM student
            WHERE student.ID LIKE %s
        """
        values = ('%' + args + '%',)
        cursor.execute(query, values)
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
    def queryStudentWithCourse(cls, args: str):
        cursor = mysql.connection.cursor()
        cursor.execute("""
            SELECT *
            FROM course
            WHERE course.coursecode like %s
        """, (args,))
        result = cursor.fetchall()
        return result
    
    @classmethod
    def queryCourseWithNoCollege(cls, args: str):
        cursor = mysql.connection.cursor()
        cursor.execute("""
            SELECT *
            FROM course
            WHERE course.coursename like %s
        """, ('%' + args + '%',))
        result = cursor.fetchall()
        return result
    
    @classmethod
    def queryCourseWithCollege(cls, args: str, college: str):
        cursor = mysql.connection.cursor()
        cursor.execute("""
            SELECT *
            FROM course
            WHERE course.coursename like %s and course.collegecode = %s
        """, ('%' + args + '%', college,))
        result = cursor.fetchall()
        return result

    @classmethod
    def queryCourse(cls, args: str):
        cursor = mysql.connection.cursor()
        cursor.execute("""
            SELECT *
            FROM course
            WHERE course.collegecode = %s
        """, (args,))
        result = cursor.fetchall()
        return result
    
    @classmethod
    def queryCourseWithCode(cls, args: str):
        cursor = mysql.connection.cursor()
        cursor.execute("""
            SELECT *
            FROM course
            WHERE course.coursecode = %s
        """, (args,))
        result = cursor.fetchall()
        return result
    
    @classmethod
    def sortBy(cls, args: str):
        cursor = mysql.connection.cursor()

        if args == "firstname":
            query = """
                SELECT *
                FROM student
                ORDER BY firstname;
            """
        elif args == "lastname":
            query = """
                SELECT *
                FROM student
                ORDER BY lastname;
            """
        elif args == "id":
            query = """
                SELECT *
                FROM student
                ORDER BY id;
            """
        elif args == "yearlevel":
            query = """
                SELECT *
                FROM student
                ORDER BY yearlevel;
            """
        else:
            query = """
                SELECT *
                FROM student
                ORDER BY gender;
            """

        cursor.execute(query)
        result = cursor.fetchall()
        return result
    
    @classmethod
    def countStudents(cls):
        try:
            cursor = mysql.connection.cursor()
            cursor.execute("SELECT COUNT(*) FROM student")
            result = cursor.fetchone()
            return result[0]  # Return the count from the result
        except Exception as e:
            print(f"Error counting students: {e}")
            return 0
        
    @classmethod
    def countPrograms(cls):
        try:
            cursor = mysql.connection.cursor()
            cursor.execute("SELECT COUNT(*) FROM course")
            result = cursor.fetchone()
            return result[0]  # Return the count from the result
        except Exception as e:
            print(f"Error counting students: {e}")
            return 0
        
    @classmethod
    def countColleges(cls):
        try:
            cursor = mysql.connection.cursor()
            cursor.execute("SELECT COUNT(*) FROM college")
            result = cursor.fetchone()
            return result[0]  # Return the count from the result
        except Exception as e:
            print(f"Error counting students: {e}")
            return 0
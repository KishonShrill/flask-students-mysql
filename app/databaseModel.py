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
    def createStudent(cls, newFirstName, newLastName, newID, newYear, newGender, newCourse: str, profilePicture):
        try:
            cursor = mysql.connection.cursor()

            # If newCourse is None, set it to NULL in the query
            if newCourse == "None":
                query = """
                    INSERT INTO student(firstname, lastname, id, yearlevel, gender, coursecode, profile_url) VALUE
                    (%s, %s, %s, %s, %s, NULL, %s);
                """
                values = (newFirstName, newLastName, newID, newYear, newGender, profilePicture)
            else:
                query = """
                    INSERT INTO student(firstname, lastname, id, yearlevel, gender, coursecode, profile_url) VALUE
                    (%s, %s, %s, %s, %s, %s, %s);
                """
                values = (newFirstName, newLastName, newID, newYear, newGender, newCourse, profilePicture)

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
        
    @classmethod
    def createCollege(cls, newName, newCode):
        try:
            cursor = mysql.connection.cursor()
            cursor.execute("""
                INSERT INTO college(collegename, collegecode) VALUE
                (%s, %s);
            """, (newName, newCode))
            mysql.connection.commit()
            return True
        
        except Exception as e:
            print(f"Error creating college: {e}")
            mysql.connection.rollback()
            return False


    """ UPDATE METHOD """    
    @classmethod
    def editStudent(cls, oldID, newFirstName, newLastName, newID, newYear, newGender, newCourse: str, profile_url: str):
        try:
            cursor = mysql.connection.cursor()

            # If newCourse is None, set it to NULL in the query
            if newCourse == "None":
                query = """
                    UPDATE student 
                    SET FirstName = %s, LastName = %s, ID = %s, YearLevel = %s, Gender = %s, CourseCode = NULL, profile_url = %s
                    WHERE ID = %s
                """
                values = (newFirstName, newLastName, newID, newYear, newGender, profile_url, oldID)
            # If newCourse is None, set it to NULL in the query
            elif profile_url == "None":
                query = """
                    UPDATE student 
                    SET FirstName = %s, LastName = %s, ID = %s, YearLevel = %s, Gender = %s, CourseCode = %s, profile_url = NULL
                    WHERE ID = %s
                """
                values = (newFirstName, newLastName, newID, newYear, newGender, newCourse, oldID)
            else:
                query = """
                    UPDATE student 
                    SET FirstName = %s, LastName = %s, ID = %s, YearLevel = %s, Gender = %s, CourseCode = %s, profile_url = %s
                    WHERE ID = %s
                """
                values = (newFirstName, newLastName, newID, newYear, newGender, newCourse, profile_url, oldID)

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
        
    @classmethod
    def editCollege(cls, oldID, newName, newCode):
        try:
            cursor = mysql.connection.cursor()
            cursor.execute("""
                UPDATE course
                SET collegename = %s, collegecode = %s
                WHERE collegecode = %s
            """, (newName, newCode, oldID))
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
        
    @classmethod
    def deleteColleges(cls, course_id: str):
        try:
            cursor = mysql.connection.cursor()
            sql = "DELETE FROM college WHERE collegecode = %s"
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
    @staticmethod
    def fetchImage(student_id):
        try:
            cursor = mysql.connection.cursor()
            query = """
            SELECT profile_url
            FROM student
            WHERE ID = %s
            """
            cursor.execute(query, (student_id,))
            result = cursor.fetchone()[0]
            return result
        except Exception as e:
            print(f"Fetch Image ERR: {e}")
    
    @classmethod
    def allStudents(cls, page):
        cursor = mysql.connection.cursor()
        
        offset = 14 * (page - 1)

        sql = """
        SELECT * 
        FROM student
        LIMIT 14
        OFFSET %s
        """
        cursor.execute(sql, (offset,))
        result = cursor.fetchall()
        
        sql = """
        SELECT COUNT(*) AS row_count
        FROM student
        """
        cursor.execute(sql)
        count = cursor.fetchone()[0]
        
        return result, count
    
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
    def queryStudentFirstNameWithCourse(cls, args: str, college: str, current_page):
        cursor = mysql.connection.cursor()
        
        offset = 14 * (current_page - 1)
        
        cursor.execute("""
        SELECT *
        FROM student
        WHERE student.FirstName LIKE %s AND student.CourseCode = %s
        LIMIT 14
        OFFSET %s
        """, ('%' + args + '%', college, offset))
        result = cursor.fetchall()
        
        sql = """
        SELECT COUNT(*) AS row_count
        FROM student
        WHERE student.FirstName LIKE %s AND student.CourseCode = %s
        """
        cursor.execute(sql, ('%' + args + '%', college))
        count = cursor.fetchone()[0]
        return result, count
    
    @classmethod
    def queryStudentLastNameWithCourse(cls, args: str, college: str, current_page):
        cursor = mysql.connection.cursor()
        offset = 14 * (current_page - 1)
        cursor.execute("""
        SELECT *
        FROM student
        WHERE student.LastName LIKE %s AND student.CourseCode = %s
        LIMIT 14
        OFFSET %s
        """, ('%' + args + '%', college, offset))
        result = cursor.fetchall()
        sql = """
        SELECT COUNT(*) AS row_count
        FROM student
        WHERE student.LastName LIKE %s AND student.CourseCode = %s
        """
        cursor.execute(sql, ('%' + args + '%', college))
        count = cursor.fetchone()[0]
        return result, count
    
    @classmethod
    def queryStudentIDWithCourse(cls, args: str, college: str, current_page):
        cursor = mysql.connection.cursor()
        offset = 14 * (current_page - 1)
        cursor.execute("""
        SELECT *
        FROM student
        WHERE student.ID LIKE %s AND student.CourseCode = %s
        LIMIT 14
        OFFSET %s
        """, ('%' + args + '%', college, offset))
        result = cursor.fetchall()
        sql = """
        SELECT COUNT(*) AS row_count
        FROM student
        WHERE student.ID LIKE %s AND student.CourseCode = %s
        """
        cursor.execute(sql, ('%' + args + '%', college))
        count = cursor.fetchone()[0]
        return result, count
    
    @classmethod
    def queryStudentYearWithCourse(cls, args: str, college: str, current_page):
        cursor = mysql.connection.cursor()
        offset = 14 * (current_page - 1)
        cursor.execute("""
        SELECT *
        FROM student
        WHERE student.YearLevel LIKE %s AND student.CourseCode = %s
        LIMIT 14
        OFFSET %s
        """, ('%' + args + '%', college, offset))
        result = cursor.fetchall()
        sql = """
        SELECT COUNT(*) AS row_count
        FROM student
        WHERE student.YearLevel LIKE %s AND student.CourseCode = %s
        """
        cursor.execute(sql, ('%' + args + '%', college))
        count = cursor.fetchone()[0]
        return result, count
    
    @classmethod
    def queryStudentGenderWithCourse(cls, args: str, college: str, current_page):
        cursor = mysql.connection.cursor()
        offset = 14 * (current_page - 1)
        cursor.execute("""
        SELECT *
        FROM student
        WHERE student.Gender LIKE %s AND student.CourseCode = %s
        LIMIT 14
        OFFSET %s
        """, ('%' + args + '%', college, offset))
        result = cursor.fetchall()
        sql = """
        SELECT COUNT(*) AS row_count
        FROM student
        WHERE student.Gender LIKE %s AND student.CourseCode = %s
        """
        cursor.execute(sql, ('%' + args + '%', college))
        count = cursor.fetchone()[0]
        return result, count
    
    @classmethod
    def queryStudentFirstName(cls, args: str, current_page):
        cursor = mysql.connection.cursor()
        offset = 14 * (current_page - 1)
        cursor.execute("""
        SELECT *
        FROM student
        WHERE student.FirstName LIKE %s
        LIMIT 14
        OFFSET %s
        """, ('%' + args + '%', offset))
        result = cursor.fetchall()
        sql = """
        SELECT COUNT(*) AS row_count
        FROM student
        WHERE student.FirstName LIKE %s
        """
        cursor.execute(sql, ('%' + args + '%',))
        count = cursor.fetchone()[0]
        return result, count
    
    @classmethod
    def queryStudentLastName(cls, args: str,current_page):
        cursor = mysql.connection.cursor()
        offset = 14 * (current_page - 1)
        cursor.execute("""
        SELECT *
        FROM student
        WHERE student.LastName LIKE %s
        LIMIT 14
        OFFSET %s
        """, ('%' + args + '%', offset))
        result = cursor.fetchall()
        sql = """
        SELECT COUNT(*) AS row_count
        FROM student
        WHERE student.LastName LIKE %s
        """
        cursor.execute(sql, ('%' + args + '%',))
        count = cursor.fetchone()[0]
        return result, count
    
    @classmethod
    def queryStudentWithID(cls, args: str, current_page):
        cursor = mysql.connection.cursor()
        offset = 14 * (current_page - 1)
        query = """
        SELECT *
        FROM student
        WHERE student.ID LIKE %s
        LIMIT 14
        OFFSET %s
        """
        values = ('%' + args + '%', offset)
        cursor.execute(query, values)
        result = cursor.fetchall()
        sql = """
        SELECT COUNT(*) AS row_count
        FROM student
        WHERE student.ID LIKE %s
        """
        cursor.execute(sql, ('%' + args + '%',))
        count = cursor.fetchone()[0]
        return result, count
    
    @classmethod
    def queryStudentCloudinaryURL(cls, args: str):
        cursor = mysql.connection.cursor()
        query = """
        SELECT profile_url
        FROM student
        WHERE student.ID LIKE %s
        """
        values = ('%' + args + '%',)
        cursor.execute(query, values)
        result = cursor.fetchall()
        return result
    
    @classmethod
    def queryStudentYear(cls, args: str,current_page):
        cursor = mysql.connection.cursor()
        offset = 14 * (current_page - 1)
        cursor.execute("""
        SELECT *
        FROM student
        WHERE student.YearLevel LIKE %s
        LIMIT 14
        OFFSET %s
        """, ('%' + args + '%', offset))
        result = cursor.fetchall()
        sql = """
        SELECT COUNT(*) AS row_count
        FROM student
        WHERE student.YearLevel LIKE %s
        """
        cursor.execute(sql, ('%' + args + '%',))
        count = cursor.fetchone()[0]
        return result, count
    
    @classmethod
    def queryStudentGender(cls, args: str, current_page):
        cursor = mysql.connection.cursor()
        offset = 14 * (current_page - 1)
        cursor.execute("""
        SELECT *
        FROM student
        WHERE student.Gender LIKE %s
        LIMIT 14
        OFFSET %s
        """, ('%' + args + '%', offset))
        result = cursor.fetchall()
        sql = """
        SELECT COUNT(*) AS row_count
        FROM student
        WHERE student.Gender LIKE %s
        """
        cursor.execute(sql, ('%' + args + '%',))
        count = cursor.fetchone()[0]
        return result, count
    
    @classmethod
    def queryStudentWithCourse(cls, args: str, current_page):
        cursor = mysql.connection.cursor()
        offset = 14 * (current_page - 1)
        cursor.execute("""
        SELECT *
        FROM student
        WHERE student.coursecode like %s
        LIMIT 14
        OFFSET %s
        """, (args, offset))
        result = cursor.fetchall()
        sql = """
        SELECT COUNT(*) AS row_count
        FROM student
        WHERE student.coursecode like %s
        """
        cursor.execute(sql, ('%' + args + '%',))
        count = cursor.fetchone()[0]
        return result, count
    
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
    def queryCollege(cls, args: str):
        cursor = mysql.connection.cursor()
        cursor.execute("""
            SELECT *
            FROM college
            WHERE college.collegename = %s
        """, (args,))
        result = cursor.fetchall()
        return result
    
    @classmethod
    def queryCollegeWithCode(cls, args: str):
        cursor = mysql.connection.cursor()
        cursor.execute("""
            SELECT *
            FROM college
            WHERE college.collegecode = %s
        """, (args,))
        result = cursor.fetchall()
        return result
    
    @classmethod
    def sortBy(cls, args: str, current_page):
        cursor = mysql.connection.cursor()
        
        offset = 14 * (current_page - 1)
        
        sql = """
        SELECT COUNT(*) AS row_count
        FROM student
        """
        cursor.execute(sql)
        count = cursor.fetchone()[0]

        if args == "firstname":
            query = """
            SELECT *
            FROM student
            ORDER BY firstname
            LIMIT 14
            OFFSET %s;
            """
        elif args == "lastname":
            query = """
            SELECT *
            FROM student
            ORDER BY lastname
            LIMIT 14
            OFFSET %s;
            """
        elif args == "id":
            query = """
            SELECT *
            FROM student
            ORDER BY id
            LIMIT 14
            OFFSET %s;
            """
        elif args == "yearlevel":
            query = """
            SELECT *
            FROM student
            ORDER BY yearlevel
            LIMIT 14
            OFFSET %s;
            """
        else:
            query = """
            SELECT *
            FROM student
            ORDER BY gender
            LIMIT 14
            OFFSET %s;
            """

        cursor.execute(query, (offset,))
        result = cursor.fetchall()
        return result, count
    
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
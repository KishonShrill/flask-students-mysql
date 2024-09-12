-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Server version:               8.0.30 - MySQL Community Server - GPL
-- Server OS:                    Win64
-- HeidiSQL Version:             12.1.0.6537
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Dumping database structure for enrolledstudents
DROP DATABASE IF EXISTS `enrolledstudents`;
CREATE DATABASE IF NOT EXISTS `enrolledstudents` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `enrolledstudents`;

-- Dumping structure for table enrolledstudents.college
DROP TABLE IF EXISTS `college`;
CREATE TABLE IF NOT EXISTS `college` (
	`CollegeName` varchar(255) NOT NULL,
	`CollegeCode` varchar(20) NOT NULL,
	PRIMARY KEY (`CollegeCode`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Dumping data for table enrolledstudents.college: ~6 rows (approximately)
INSERT INTO `college` (`CollegeName`, `CollegeCode`) VALUES
	('College of Arts and Social Sciences', 'CASS'),
	('College of Economics, Business, and Accountancy', 'CEBA'),
	('College of Science and Mathematics', 'CSM'),
	('College of Computer Studies', 'CCS'),
	('College of Engineering and Technology', 'CET'),
	('College of Nursing', 'CON'),
	('College of Education', 'CED');

-- Dumping structure for table enrolledstudents.course
DROP TABLE IF EXISTS `course`;
CREATE TABLE IF NOT EXISTS `course` (
  `CourseName` varchar(255) NOT NULL,
  `CourseCode` varchar(20) NOT NULL,
	`CollegeCode` varchar(20) NOT NULL,
  PRIMARY KEY (`CourseCode`),
	KEY `fk_course_college` (`CollegeCode`),
  CONSTRAINT `fk_course_college` FOREIGN KEY (`CollegeCode`) REFERENCES `college` (`CollegeCode`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Dumping data for table enrolledstudents.course: ~11 rows (approximately)
INSERT INTO `course` (`CourseName`, `CourseCode`, `CollegeCode`) VALUES
	('Bachelor of Arts in English Language Studies', 'BAELS', 'CASS'),
	('Bachelor of Arts in Filipino', 'BAF', 'CASS'),
	('Bachelor of Arts in History', 'BAH', 'CASS'),
	('Bachelor of Arts in Panitikan', 'BAP', 'CASS'),
	('Bachelor of Arts in Political Science', 'BAPolSci', 'CASS'),
	('Bachelor of Arts in Psychology', 'BAPsych', 'CASS'),
	('Bachelor of Arts in Sociology', 'BASoc', 'CASS'),
	('Bachelor of Science in Psychology', 'BSPsych', 'CASS'),
	('Bachelor of Science in Philosophy', 'BSPhil', 'CASS'),
	('Bachelor of Science in Accountancy', 'BSA', 'CEBA'),
	('Bachelor of Science in Economics', 'BAEcon', 'CEBA'),
	('Bachelor of Science in Entrepreneurship', 'BSEntrep', 'CEBA'),
	('Bachelor of Science in Hospitality Management', 'BSHM', 'CEBA'),
	('Bachelor of Science in Business Administration', 'BSBA', 'CEBA'),
	('Bachelor of Science in Animal Biology', 'BSAnimalBio', 'CSM'),
	('Bachelor of Science in Plant Biology', 'BSPlantBio', 'CSM'),
	('Bachelor of Science in Biodiversity', 'BSBiodiv', 'CSM'),
	('Bachelor of Science in Chemistry', 'BSChem', 'CSM'),
	('Bachelor of Science in Marine Biology', 'BSMarBio', 'CSM'),
	('Bachelor of Science in Mathematics', 'BSMath', 'CSM'),
	('Bachelor of Science in Physics', 'BSPhys', 'CSM'),
	('Bachelor of Science in Statistics', 'BSStat', 'CSM'),
	('Bachelor of Science in Computer Application', 'BSCA', 'CCS'),
	('Bachelor of Science in Computer Science', 'BSCS', 'CCS'),
	('Bachelor of Science in Information Systems', 'BSIS', 'CCS'),
	('Bachelor of Science in Information Technology', 'BSIT', 'CCS'),
	('Bachelor of Science in Nursing', 'BSN', 'CON'),
	('Bachelor of Science in Ceramics Engineering', 'BSCerE', 'CET'),
	('Bachelor of Science in Checmical Engineering', 'BSChemEng', 'CET'),
	('Bachelor of Science in Civil Engineering', 'BSCE', 'CET'),
	('Bachelor of Science in Computer Engineering', 'BSComEng', 'CET'),
	('Bachelor of Science in Electrical Engineering', 'BSEE', 'CET'),
	('Bachelor of Science in Electronics Engineering', 'BSECE', 'CET'),
	('Bachelor of Science in Environment Engineering', 'BSEnvEng', 'CET'),
	('Bachelor of Science in Industrial Automation and Mechanism', 'BSIAM', 'CET'),
	('Bachelor of Science in Mechanical Engineering', 'BSME', 'CET'),
	('Bachelor of Science in Metallurgical Engineering', 'BSMetE', 'CET'),
	('Bachelor of Science in Mining Engineering', 'BSEM', 'CET'),
	('Bachelor of Elementary Education', 'BEEd', 'CED'),
	('Bachelor of Secondary Education', 'BSEd', 'CED'),
	('Bachelor of Technical-Vocation Teacher Education', 'BTVTEd', 'CED'),
	('Bachelor of Technology and Livelihood Education', 'BTLEd', 'CED'),
	('Bachelor of Physical Education', 'BPEd', 'CED');

-- Dumping structure for table enrolledstudents.student
DROP TABLE IF EXISTS `student`;
CREATE TABLE IF NOT EXISTS `student` (
  `FirstName` varchar(199) NOT NULL,
	`LastName` varchar(199) NOT NULL,
  `ID` char(9) NOT NULL,
  `YearLevel` char(1) NOT NULL,
  `Gender` varchar(2) NOT NULL,
  `CourseCode` varchar(20) DEFAULT NULL,
  UNIQUE KEY `unique_name` (`FirstName`, `LastName`),
  KEY `fk_student_course` (`CourseCode`),
  CONSTRAINT `fk_student_course` FOREIGN KEY (`CourseCode`) REFERENCES `course` (`CourseCode`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Dumping data for table enrolledstudents.student: ~101 rows (approximately)
INSERT INTO `student` (`FirstName`, `LastName`, `ID`, `YearLevel`, `Gender`, `CourseCode`) VALUES
	("Michael Christopher", "Rodriguez", "2023-6466", "5", "NB", "BSCS"),
	("Isabella Grace", "Smith", "2022-7358", "4", "F", "BSN"),
	("John Joseph", "Johnson", "2024-3508", "2", "F", "BSAnimalBio"),
	("William Christopher", "Garcia", "2020-3442", "3", "NB", "BSPlantBio"),
	("Alexander Amelia", "Martinez", "2022-0789", "3", "F", "BSCerE"),
	("Emma Elizabeth", "Jones", "2024-1465", "3", "M", "BAEcon"),
	("Emma Charlotte", "Martinez", "2023-4337", "3", "F", "BAEcon"),
	("John Christopher", "Martinez", "2022-8975", "4", "F", "BAH"),
	("Ava Daniel", "Smith", "2021-4020", "1", "M", "BSIAM"),
	("William Christopher", "Smith", "2023-4234", "2", "NB", "BAEcon"),
	("Ava David", "Smith", "2023-8389", "3", "NB", "BAH"),
	("William David", "Garcia", "2024-4606", "4", "M", "BSCS"),
	("Alexander Matthew", "Rodriguez", "2023-4564", "3", "NB", "BSPhys"),
	("Alexander Amelia", "Brown", "2023-4544", "3", "M", "BSIS"),
	("Isabella Elizabeth", "Garcia", "2021-1859", "3", "F", "BSIT"),
	("John David", "Jones", "2023-1755", "3", "F", "BSBA"),
	("Isabella David", "Miller", "2021-8295", "1", "F", "BSPhys"),
	("Ava Amelia", "Davis", "2020-4358", "1", "F", "BSChemEng"),
	("John Joseph", "Jones", "2020-5350", "5", "NB", "BSEntrep"),
	("Michael Joseph", "Jones", "2023-0274", "1", "NB", "BAH"),
	("Emma Matthew", "Smith", "2020-2837", "3", "NB", "BAP"),
	("Ava Charlotte", "Rodriguez", "2024-4900", "4", "M", "BAF"),
	("William Christopher", "Brown", "2020-8964", "2", "F", "BSME"),
	("Ava David", "Johnson", "2023-2375", "5", "M", "BSHM"),
	("James Matthew", "Smith", "2022-6015", "2", "NB", "BSPhil"),
	("Sophia David", "Garcia", "2022-7072", "5", "F", "BSCA"),
	("Emma Grace", "Smith", "2021-7085", "5", "F", "BTVTEd"),
	("Emma Joseph", "Davis", "2021-0111", "1", "M", "BTVTEd"),
	("Michael David", "Rodriguez", "2021-4334", "5", "M", "BSHM"),
	("Olivia Elizabeth", "Garcia", "2022-8101", "4", "M", "BSCA"),
	("Isabella Elizabeth", "Martinez", "2024-4930", "5", "M", "BSChem"),
	("Alexander Christopher", "Brown", "2023-1640", "2", "M", "BPEd"),
	("Olivia Mia", "Brown", "2024-3356", "4", "NB", "BAELS"),
	("John Joseph", "Miller", "2020-6416", "5", "NB", "BSIT"),
	("Michael Elizabeth", "Davis", "2024-9916", "2", "NB", "BSEntrep"),
	("Ava David", "Conquer", "2022-4047", "5", "F", "BSCerE"),
	("Michael Grace", "Brown", "2022-5257", "3", "NB", "BSEd"),
	("Ava Joseph", "Garcia", "2021-4467", "3", "NB", "BAP"),
	("Michael David", "Squirell", "2024-2078", "2", "F", "BSEnvEng"),
	("Michael Christopher", "Garcia", "2020-7977", "1", "M", "BSEd"),
	("Olivia Elizabeth", "Martinez", "2022-3477", "4", "M", "BSECE"),
	("John Amelia", "Williams", "2020-2689", "4", "M", "BAELS"),
	("Isabella Christopher", "Rodriguez", "2021-0369", "3", "M", "BEEd"),
	("Sophia Amelia", "Garcia", "2022-2806", "4", "M", "BAPolSci"),
	("Emma Christopher", "Jones", "2023-8554", "1", "M", "BTLEd"),
	("Emma Charlotte", "Brown", "2023-0281", "2", "F", "BSCerE"),
	("Michael David", "Davis", "2020-4152", "2", "F", "BAPolSci"),
	("William Joseph", "Johnson", "2024-9275", "2", "M", "BSCerE"),
	("James Elizabeth", "Brown", "2024-0036", "4", "M", "BASoc"),
	("Michael Joseph", "Davis", "2021-1287", "2", "F", "BAPolSci"),
	("Isabella Charlotte", "Miller", "2024-7495", "3", "F", "BSCE"),
	("Ava Christopher", "Jones", "2020-5956", "4", "NB", "BSN"),
	("Isabella Christopher", "Smith", "2020-8070", "4", "NB", "BAELS"),
	("Sophia David", "Williams", "2020-4650", "1", "NB", "BSPlantBio"),
	("Sophia Grace", "Williams", "2021-7235", "4", "M", "BSEd"),
	("Alexander Daniel", "Jones", "2021-9054", "4", "NB", "BAH"),
	("Sophia Charlotte", "Miller", "2022-2409", "3", "F", "BSN"),
	("Isabella Christopher", "Martinez", "2022-5722", "4", "NB", "BSME"),
	("James Matthew", "Williams", "2024-8102", "5", "F", "BSIS"),
	("William Grace", "Miller", "2024-0030", "4", "NB", "BTLEd"),
	("Ava David", "Smithereens", "2021-2703", "3", "F", "BSMetE"),
	("Alexander Grace", "Martinez", "2023-0088", "1", "F", "BSIS"),
	("Olivia Elizabeth", "Rodriguez", "2022-8425", "1", "M", "BSBA"),
	("Isabella Matthew", "Davis", "2020-8439", "4", "M", "BSEE"),
	("James Christopher", "Brown", "2021-2392", "4", "NB", "BSCA"),
	("William Elizabeth", "Smith", "2023-5096", "1", "F", "BSECE"),
	("Isabella Joseph", "Rodriguez", "2020-8358", "5", "NB", "BSEE"),
	("John Christopher", "Rodriguez", "2024-1104", "4", "M", "BSEE"),
	("Sophia David", "Brown", "2021-9811", "2", "NB", "BAELS"),
	("Alexander Amelia", "Rainbow", "2021-4213", "1", "F", "BSCE"),
	("Emma Grace", "Davis", "2023-9183", "1", "M", "BAPolSci"),
	("Sophia Grace", "Jones", "2023-9328", "1", "NB", "BSIT"),
	("Olivia Joseph", "Smith", "2021-5876", "5", "NB", "BTLEd"),
	("Isabella David", "Johnson", "2020-5631", "5", "F", "BPEd"),
	("Sophia Matthew", "Rodriguez", "2024-0285", "5", "NB", "BSME"),
	("James Grace", "Jones", "2022-1524", "3", "F", "BTVTEd"),
	("William Charlotte", "Johnson", "2022-9540", "3", "NB", "BSA"),
	("William David", "Hope", "2023-1531", "2", "F", "BSCE"),
	("William Joseph", "Williams", "2022-3211", "2", "NB", "BSEd"),
	("Olivia Grace", "Martinez", "2022-0308", "1", "F", "BSCA"),
	("Sophia Joseph", "Davis", "2022-5267", "2", "F", "BAP"),
	("John Mia", "Brown", "2020-1286", "4", "F", "BSBA"),
	("John Matthew", "Smith", "2022-8475", "2", "F", "BAELS"),
	("Alexander Christopher", "Rodriguez", "2021-6988", "2", "F", "BSME"),
	("Isabella Charlotte", "Brown", "2020-5506", "1", "NB", "BSEd"),
	("Michael Christopher", "Jones", "2024-1226", "3", "M", "BSA"),
	("Sophia Matthew", "Martinez", "2020-6210", "5", "F", "BSIAM"),
	("William Charlotte", "Jones", "2020-4411", "4", "M", "BPEd"),
	("Olivia Matthew", "Miller", "2023-8491", "1", "NB", "BSEnvEng"),
	("William Matthew", "Jones", "2021-4201", "4", "NB", "BSIS"),
	("Alexander David", "Miller", "2020-5404", "5", "M", "BSEnvEng"),
	("Michael Amelia", "Garcia", "2024-6831", "3", "F", "BSEE"),
	("John Joseph", "Digger", "2024-9981", "5", "F", "BSPhil"),
	("Sophia Christopher", "Davis", "2021-3019", "3", "F", "BSHM"),
	("Ava Joseph", "Brown", "2023-6523", "2", "NB", "BAPsych"),
	("Alexander Daniel", "Johnson", "2020-9728", "5", "NB", "BTLEd"),
	("James Mia", "Johnson", "2024-1940", "3", "F", "BSPhys"),
	("James Mia", "Smith", "2023-7146", "3", "F", "BSPhys"),
	("John Mia", "Garcia", "2020-0740", "4", "F", "BSPhys"),
	("Olivia Charlotte", "Johnson", "2020-9482", "5", "F", "BSIS");


/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;

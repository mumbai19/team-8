CREATE TABLE `Student` (
	`student_id` INT NOT NULL AUTO_INCREMENT,
	`student_name` varchar(255),
	`parent_name` varchar(255),
	`phone_no` INT NOT NULL,
	`standard` varchar(255) NOT NULL,
	`address` varchar(255) NOT NULL,
	`mentor_id` INT(255) NOT NULL,
	PRIMARY KEY (`student_id`)
);

CREATE TABLE `Mentor` (
	`mentor_id` INT NOT NULL AUTO_INCREMENT,
	`mentor_name` varchar(255),
	`username` varchar(255),
	`password` varchar(255) NOT NULL,
	`course_id` INT(255) NOT NULL,
	PRIMARY KEY (`mentor_id`)
);

CREATE TABLE `Saving` (
	`saving_id` INT NOT NULL AUTO_INCREMENT,
	`savings` INT NOT NULL,
	`student_id` INT NOT NULL,
	`saving_date` DATE NOT NULL,
	PRIMARY KEY (`saving_id`)
);

CREATE TABLE `Course` (
	`course_id` INT NOT NULL AUTO_INCREMENT,
	`course_name` varchar(255) NOT NULL,
	PRIMARY KEY (`course_id`)
);

CREATE TABLE `Activity` (
	`activity_id` INT NOT NULL AUTO_INCREMENT,
	`theme` varchar(255) NOT NULL,
	`activity_name` varchar(255) NOT NULL,
	`activity_description` varchar(255) NOT NULL,
	`mentor_id` INT(255) NOT NULL,
	PRIMARY KEY (`activity_id`)
);

CREATE TABLE `Attendance` (
	`student_id` INT NOT NULL,
	`mentor_id` INT NOT NULL,
	`attendance_date` DATE NOT NULL,
	`present` INT NOT NULL,
	PRIMARY KEY (`student_id`,`mentor_id`)
);

CREATE TABLE `Stars` (
	`student_id` INT NOT NULL,
	`mentor_id` INT NOT NULL,
	`attribute` varchar(255) NOT NULL,
	`no_stars` INT(255) NOT NULL,
	`star_date` DATE NOT NULL,
	PRIMARY KEY (`student_id`,`mentor_id`)
);

CREATE TABLE `Evaluate` (
	`student_id` INT NOT NULL,
	`mentor_id` INT NOT NULL,
	`marks` INT NOT NULL,
	PRIMARY KEY (`student_id`,`mentor_id`)
);

ALTER TABLE `Student` ADD CONSTRAINT `Student_fk0` FOREIGN KEY (`mentor_id`) REFERENCES `Mentor`(`mentor_id`);

ALTER TABLE `Mentor` ADD CONSTRAINT `Mentor_fk0` FOREIGN KEY (`course_id`) REFERENCES `Course`(`course_id`);

ALTER TABLE `Saving` ADD CONSTRAINT `Saving_fk0` FOREIGN KEY (`student_id`) REFERENCES `Student`(`student_id`);

ALTER TABLE `Course` ADD CONSTRAINT `Course_fk0` FOREIGN KEY (`course_name`) REFERENCES `Student`(`student_id`);

ALTER TABLE `Activity` ADD CONSTRAINT `Activity_fk0` FOREIGN KEY (`mentor_id`) REFERENCES `Mentor`(`mentor_id`);

ALTER TABLE `Attendance` ADD CONSTRAINT `Attendance_fk0` FOREIGN KEY (`student_id`) REFERENCES `Student`(`student_id`);

ALTER TABLE `Attendance` ADD CONSTRAINT `Attendance_fk1` FOREIGN KEY (`mentor_id`) REFERENCES `Mentor`(`mentor_id`);

ALTER TABLE `Stars` ADD CONSTRAINT `Stars_fk0` FOREIGN KEY (`student_id`) REFERENCES `Student`(`student_id`);

ALTER TABLE `Stars` ADD CONSTRAINT `Stars_fk1` FOREIGN KEY (`mentor_id`) REFERENCES `Mentor`(`mentor_id`);

ALTER TABLE `Evaluate` ADD CONSTRAINT `Evaluate_fk0` FOREIGN KEY (`student_id`) REFERENCES `Student`(`student_id`);

ALTER TABLE `Evaluate` ADD CONSTRAINT `Evaluate_fk1` FOREIGN KEY (`mentor_id`) REFERENCES `Mentor`(`mentor_id`);


CREATE TABLE Course(
    id number not null ,
    name varchar2(100) ,
    url varchar2(100) ,
    price float
);

CREATE TABLE Info(
    id number not null ,
    lectures_num number ,
    level_name varchar2(100) ,
    duration number,
    course_id number not null
);

CREATE TABLE Subject(
    subject varchar2(100) not null
);

CREATE TABLE Udemy(
    id number not null,
    course_id number not null,
    subject varchar2(100) not null
);



--alter course
ALTER TABLE Course ADD CONSTRAINT course_pk PRIMARY KEY(id);

--alter info
ALTER TABLE Info ADD CONSTRAINT fk_course_info foreign key (course_id) references Course(id);
ALTER TABLE Info ADD CONSTRAINT info_pk PRIMARY KEY(id);

--alter subject
ALTER TABLE Subject ADD CONSTRAINT subject_pk PRIMARY KEY(subject);

--alter udemy
ALTER TABLE Udemy ADD CONSTRAINT udemy_pk PRIMARY KEY(id);

ALTER TABLE Udemy ADD CONSTRAINT fk_course foreign key (course_id) references Course(id);

ALTER TABLE Udemy ADD CONSTRAINT fk_subject foreign key (subject) references Subject(Subject);


--drop table:

drop table udemy;
drop table subject;
drop table info;
drop table course;
--- Create a new schema for family data
drop schema if exists family_db;
create schema family_db;
use family_db;


--- Table for grandfather and his siblings
create table grandfather (
	id int primary key,
    name varchar(100),
	birth_date date,
    age INT,
    email varchar(100),
    alive boolean,
    number_of_brothers int,
    number_of_sisters int,
    wealth decimal(12, 2),
    death_date date
);

--- Table for siblings of grandfatehr
create table grandfather_siblings (
	id int primary key not null,
    grandparent_id int,
    name varchar(100),
    gender enum('male', 'female'),
    spouse_name varchar(100),
    number_of_childern int,
    wealth decimal(12,2),
    birth_date date,
    age int,
    email varchar(100),
    alive boolean,
    death_date date,
    foreign key (grandparent_id) references grandfather(id)
);


--- Table for father data
create table father (
	id int primary key,
    name varchar(100),
    birth_date date,
    age int,
    number_of_brothers int,
    number_of_sisters int,
    wealth decimal(12, 2),
    email varchar(100),
    alive boolean
);


--- Table for father's gift history
create table father_gifts (
	id int primary key,
    father_id int, 
    year YEAR,
    gift_description varchar(255),
    from_relative_name varchar(100),
    estimated_value decimal(10, 2),
    foreign key (father_id) references father(id)
);


--- Insert data for grandfather
INSERT INTO grandfather values
(1, 'Abdul Karim', '1930-02-15', 94, 'abdulKarim@fake.com',false, 7, 3, 150000.00, '2024-03-01');

--- Insert data for GrandFather_siblings
INSERT INTO grandfather_siblings values
(106, 1, 'Abdul Karim', 'Male', 'Fatema Begum', 5, 2500000, '1940-05-12', 85, 'abdulkarim@gmail.com', FALSE, '2022-11-10'),

(107, 1, 'Rashida Khatun', 'Female', 'Habibur Rahman', 4, 1800000, '1945-08-22', 80, 'rashida@gmail.com', TRUE, NULL),

(108, 1, 'Mohammad Ali', 'Male', 'Shirin Akter', 3, 3000000, '1938-01-15', 87, 'mohammadali@gmail.com', FALSE, '2020-07-05'),

(109, 1, 'Nurjahan Begum', 'Female', 'Abdur Rahman', 6, 2200000, '1942-03-30', 83, 'nurjahan@gmail.com', TRUE, NULL),

(110, 1, 'Anwar Hossain', 'Male', 'Selina Begum', 2, 1500000, '1950-09-18', 75, 'anwar@gmail.com', TRUE, NULL);


--- Insert data for father
insert into father values
(1, 'Mizanur Rahman', '1965-05-25', 60, 4, 2, 1200000.00, 'mizan@mail.com', true);


--- Insert father's gift history
insert into father_gifts values
(1, 1, 2010, 'Gold Watch', 'uncle Habib', 25000.00),
(2, 1, 2015, 'Land in village', 'Uncle Jabed', 350000.00),
(3, 1, 2018, 'Cash gift for house', 'Aunty Farida', 500000.00),
(4, 1, 2022, 'Laptop', 'Brother Tasin', 52000.00);



create database pharmacy;

use pharmacy;

-- User Table
c gymreate table userInfo(
UserID INT(5) Primary Key, 
Name Varchar(30), 
Age INT(3) check (age > 10 and age < 100), 
Gender VARCHAR(15) check (gender = "M" or gender = "F"));

-- Insert values in user table
insert into userinfo values
(1, "Alice Johnson", 26, "F"),
(2, "Benjamin Martinez", 51, "M"),
(3, "Chloe Thompokedexpson", 46, "F"),
(4, "Daniel Lee", 18, "M"),
(5, "Emily Davis", 61, "F"),
(6, "Ethan Clark", 48, "M"),
(7, "Fiona Rodriguez", 52, "F"),
(8, "Gavin Wright", 26, "M"),
(9, "Hannah Adams", 32, "F"),
(10, "Isaac Scott", 48, "M"),
(11, "Jessica Hall", 30, "F"),
(12, "Kevin Allen", 61, "M"),
(13, "Lily Baker", 42, "F"),
(14, "Hannah Adams", 32, "F"),
(15, "Mason Lewis", 30, "M"),
(16, "Natalie Garcia", 52, "F"),
(17, "Olivia King", 46, "F"),
(18, "Parker Young", 28, "M"),
(19, "Quinn Harris", 54, "F"),
(20, "Riley Turner", 30, "F"),
(21, "Sophia White", 51, "F"),
(22, "Tyler Moore", 27, "M"),
(23, "Victoria Hill", 51, "F"),
(24, "William Carter", 30, "M"),
(25, "Xander Brown", 59, "M"),
(26, "Yara Flores", 36, "F"),
(27, "Zachary Taylor", 61, "M"),
(28, "Ava Mitchell", 26, "F"),
(29, "Brandon Nelson", 46, "M"),
(30, "Dylan Wilson", 25, "M");

-- Product Table
create table product(
ProductID INT(5) primary key, 
Price INT(5), 
Product_Name VARCHAR(30), 
Type VARCHAR(25), 
Quantity INT(4));

-- Insert Value in Product Table
insert into product values
(1, 50, "Paracetamol", "Tablet", 100),
(2, 100, "Raricap 100 Tablet", "Tablet", 0),
(3, 81, "Cofsils Cough Syrup", "Syrup", 78),
(4, 149, "Fast Relief", "Spray", 23),
(5, 41, "NVM Tablet", "Tablet", 0),
(6, 4, "Disprin Tablet", "Tablet", 190),
(7, 148, "Zedex Plus", "Syrup", 500),
(8, 40, "Naselin Spray", "Spray", 0);

-- Order Item Table
create table orderitem(
OrderID INT(5) Primary Key, 
UserID INT(5),
productID INT(5), 
DID INT(5),
Quantity INT(4), 
SubTotal INT(5), 
Status VARCHAR(30), 
ShipDate DATE, 
ShippingAddress Varchar(50),
Foreign Key (productID) references product(productID),
Foreign key(userID) references userinfo(userID),
foreign key(did) references doctor(did));

-- Insert values in orderitem table
INSERT INTO orderitem VALUES
(1, 1, 1, 1, 2, 200, 'Process', '2024-02-18', 'Delhi'),
(2, 2, 2, 2, 1, 50, 'Pending', '2024-12-15', 'Mumbai'),
(3, 3, 3, 3, 3, 300, 'Shipped', '2024-04-16', 'Delhi'),
(4, 4, 4, 4, 4, 400, 'Process', '2024-04-17', 'Bangalore'),
(5, 5, 2, 5, 2, 150, 'Delivered', '2024-06-18', 'Chennai'),
(6, 6, 1, 4, 1, 75, 'Pending', '2024-07-19', 'Mumbai'),
(7, 7, 3, 2, 3, 225, 'Process', '2024-03-20', 'Delhi'),
(8, 8, 1, 3, 2, 100, 'Shipped', '2024-11-21', 'Bangalore'),
(9, 1, 4, 3, 1, 50, 'Delivered', '2024-09-22', 'Delhi'),
(10, 2, 3, 3, 4, 200, 'Process', '2024-05-23', 'Chennai'),
(11, 1, 1, 1, 2, 150, 'Pending', '2024-03-24', 'Mumbai'),
(12, 2, 2, 2, 3, 225, 'Shipped', '2024-01-25', 'Delhi'),
(13, 3, 3, 3, 1, 50, 'Delivered', '2024-04-26', 'Bangalore'),
(14, 4, 4, 4, 2, 100, 'Process', '2024-03-27', 'Mumbai'),
(15, 5, 2, 5, 4, 400, 'Pending', '2024-04-28', 'Chennai');


-- Doctor Table
create table doctor(
DID INT(5) Primary Key, 
Name Varchar(30), 
Age INT(3), 
Specialization VARCHAR(25), 
Total_Payment INT(8));

insert into doctor values
(1, "Ramesh", 51, "ENT", 5000000),
(2, "Raghav", 40, "Dentist", 7000000),
(3, "Mohit", 56, "Surgeon", 900000),
(4, "Abhijit", 42, "ENT", 600000),
(5, "Tanish", 51, "Physio", 2500000),
(6, "gsjdga", 23, "ENT", 5250000),
(7, "Navneet", 45, "Dentist", 850000),
(8, "mandal", 46, "ENT", 7845600),
(9, "jhanta", 61, "Surgeon", 950000),
(10, "uiha", 53, "ENT", 8500000);

-- 1. Different specialization of doctor
select spEciAlization, count(*) as doctor_count from doctor group by specialization;

-- 2. Amount by specialization
select specialization, Sum(Total_payment) as Total_Amount from doctor group by specialization; 

-- 3. Total payment in different months
select extract(Month from shipdate) as Month, 
sum(subtotal) as Total_payment from orderitem 
group by extract(Month from shipdate) order by month; 

-- 4. Different type of status
select Status, count(*) as Total from orderitem group by status; 

-- 5. Where are the orderes delivered most
select ShippingAddress, count(*) as Count from orderitem group by shippingaddress; 

-- 6. Amount / Status
select status, sum(Subtotal) as Amount from orderitem group by status;

-- 7. Quantity wise product
select product_name, quantity, price from product limit 5;

-- 8. Products which need restocking
select product_name, price from product where quantity = 0;

-- 9. Top 5 costly meds
select product_name, price from product order by price desc limit 5;

-- 10. Gender of users
select gender, count(*) as total from userinfo group by gender;
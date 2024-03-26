--create table in the current database
-- create database
CREATE IF NOT EXISTS DATABASE hbtn_0c_0;
--set current database
USE hbtn_0c_0;
--create table
CREATE TABLE first_table IF NOT EXISTS states (id INT UNIQUE NOT NULL AUTO_INCREMENT, name VARCHAR(256), PROMARY KEY(id)); 

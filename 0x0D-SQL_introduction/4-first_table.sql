--create table in the current database
-- create database
CREATE IF NOT EXISTS DATABASE hbtn_0c_0;
--set current database
USE hbtn_0c_0;
--create table
CREATE TABLE IF NOT EXISTS first_table (id INT UNIQUE NOT NULL AUTO_INCREMENT, name VARCHAR(256) NOT NULL, PRIMARY KEY(id)); 

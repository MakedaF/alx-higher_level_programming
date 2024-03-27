-- Creates database hbtn_0d_usa and table states in the database
-- Creates hbtn_0d_usa database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- use hbtn_0d_usa
USE hbtn_0d_usa;
-- Create states tables
CREATE TABLE IF NOT EXISTS states (id INT UNIQUE NOT NULL AUTO_INCREMENT, name VARCHAR(256) NOT NULL, PRIMARY KEY(id));

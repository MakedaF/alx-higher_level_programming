--Creates hbtn_0d_2 datbase and user_0d_02
--Create database
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
--Create user
CREATE USER IF NOT EXISTS user_0d_2@hbtn_0d_2 IDENTIFIED BY 'user_0d_2_pwd';
--Grant SELECT privilege
GRANT SELECT ON hbtn_0d_2.* TO user_0d_2@hbtn_0d_2;

--creates user "user 0d 1" with all privilages
CREATE USER IF NOT EXISTS `user_0d_1`@`localhost` IDENTIFIED BY `user_0d_1_pwd`;
--Grant privilege
GRANT ALL PRIVILEGES ON *.* TO `user_0d_1`@`localhost`;
FLUSH PRIVILEGES;


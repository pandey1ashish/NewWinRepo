show databases;
use sakila;
show tables;

show databases;
use sakila;
CREATE TABLE `sakila`.`tblUser` (
`UserId` INT NOT NULL AUTO_INCREMENT,
`UserName` VARCHAR(45) NULL,
`Password` VARCHAR(45) NULL,
PRIMARY KEY (`UserId`));
select * from tblUser;

DROP procedure IF EXISTS `spCreateUser`;

DELIMITER $$
USE `sakila`$$
CREATE PROCEDURE `spCreateUser` (IN p_Username varchar(50), IN p_Password varchar(50))
BEGIN
	if ( select exists (select 1 from tblUser where UserName = p_username) ) THEN
		select 'Username Exists !!';
	ELSE
		insert into tblUser(UserName, Password)
		values(p_Username, p_Password);
	END IF;
END$$
DELIMITER ;

select version();
SHOW PRIVILEGES;

show create procedure spCreateUser;

select count(*) from actor;
select * from actor where first_name = 'NICK';
select Concat(first_name,' ', last_name) from actor where actor_id = 2;

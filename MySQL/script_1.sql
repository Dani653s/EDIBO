USE db24;

DELIMITER $$
CREATE TRIGGER MyTBL_9a_guard1 BEFORE INSERT ON MyTBL_9a
FOR EACH ROW
BEGIN
DECLARE a varchar(100);
SELECT CURRENT_USER() INTO @a;
SIGNAL SQLSTATE "50000" SET message_text=@a;
END;$$
DELIMITER ;

INSERT INTO MyTBL_9a (Title) VALUE ("AAA");


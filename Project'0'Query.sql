-- Select all rows from table
SELECT * FROM Proj.mytable;

-- select a row from table
SELECT *from Proj.mytable limit 1; 

-- select limited rows from table
SELECT *from mytable limit 9;

-- delete command
DELETE from mytable
where meal_id = 1109;
Select *from mytable;

-- update command
UPDATE mytable 
SET category = "Sea food" where meal_id = 1180;
Select *from mytable;

-- insert command
INSERT into mytable values(1109, "Snacks","Italian");
Select *from mytable;

-- drop a table
drop table mytable;
Select *from mytable;

-- Sort in an order
SELECT *FROM mytable
ORDER BY cuisine DESC;

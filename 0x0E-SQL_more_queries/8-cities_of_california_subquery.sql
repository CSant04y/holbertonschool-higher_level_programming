-- script that lists all the cities of California that can be found in the database hbtn_0d_usa.
-- lists all cities in california;
SET @v1 := (SELECT id FROM states WHERE name = "California");
SELECT id, name FROM cities WHERE state_id = @v1;

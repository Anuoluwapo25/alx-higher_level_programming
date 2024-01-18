-- Use the hbtn_0d_usa database
-- Select cities of California without using JOIN

SELECT id, name
FROM cities
WHERE state_id =  (SELECT id 
	FROM states
	WHERE name = 'California')
GROUP BY cities.id
ORDER BY cities.id ASC;


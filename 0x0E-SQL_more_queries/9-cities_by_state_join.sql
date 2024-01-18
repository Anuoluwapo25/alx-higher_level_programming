-- Use the hbtn_0d_usa database
-- Select cities and corresponding state names

SELECT cities.id, cities.name, states.name
FROM cities
JOIN states WHERE state_id = states.id
ORDER BY cities.id ASC;


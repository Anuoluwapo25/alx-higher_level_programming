--  script that displays the top 3 of cities temperature
-- during July and August ordered by temperature (descending)

SELECT city, AVG(score) AS avg_temp
FROM temperature
WHERE MONTH(date) IN (7, 8) 
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;

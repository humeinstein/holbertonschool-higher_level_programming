-- show all score occurences
SELECT score,COUNT(score) AS number FROM second_table GROUP BY number DESC;

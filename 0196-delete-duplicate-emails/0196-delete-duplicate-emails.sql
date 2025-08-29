/* Write your T-SQL query statement below */

DELETE FROM PERSON 
WHERE ID NOT IN (SELECT MIN(id) AS MINID
    FROM Person
    GROUP BY email
    )

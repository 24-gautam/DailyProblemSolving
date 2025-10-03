/* Write your T-SQL query statement below */

/* Write your T-SQL query statement below */

SELECT
DISTINCT
    P.product_id,
    P.product_name
FROM
    Product P
INNER JOIN
    Sales S ON P.product_id = S.product_id
AND
    NOT EXISTS
        (
            SELECT
                1
            FROM
                Sales SS
            WHERE
                SS.product_id = S.product_id
            AND
               (SS.sale_date < '2019-01-01' OR SS.sale_date > '2019-03-31') 
        )


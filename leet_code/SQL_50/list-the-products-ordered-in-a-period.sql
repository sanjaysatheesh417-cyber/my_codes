#https://leetcode.com/problems/list-the-products-ordered-in-a-period/?envType=study-plan-v2&envId=top-sql-50

solution:
WITH final AS (SELECT
    P.product_name,
    SUM(O.unit) AS unit
FROM Products P
JOIN Orders O
    ON O.product_id = P.product_id
WHERE order_date >= '2020-02-01' AND order_date < '2020-03-01'
GROUP BY P.product_id)

SELECT
    *
FROM final
WHERE unit >= 100;

#https://leetcode.com/problems/product-sales-analysis-i/submissions/1950186436/?envType=study-plan-v2&envId=top-sql-50

solution:
SELECT
    P.product_name,
    S.year,
    S.price
FROM Sales S
JOIN Product P
    ON S.product_id = P.product_id
GROUP BY sale_id,year;

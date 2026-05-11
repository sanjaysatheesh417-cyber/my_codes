#https://leetcode.com/problems/customers-who-bought-all-products/submissions/2000640487/?envType=study-plan-v2&envId=top-sql-50

solution:
SELECT customer_id
FROM Customer
GROUP BY customer_id
HAVING COUNT(DISTINCT product_key) = (SELECT COUNT(*) FROM Product);

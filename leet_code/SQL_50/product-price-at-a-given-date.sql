#https://leetcode.com/problems/product-price-at-a-given-date/description/?envType=study-plan-v2&envId=top-sql-50

solution:
WITH RankedPrices AS (
    SELECT
        product_id,
        new_price,
        ROW_NUMBER() OVER(PARTITION BY product_id ORDER BY change_date DESC) as rn
    FROM Products
    WHERE change_date <= '2019-08-16'
)

SELECT 
    product_id, 
    new_price AS price
FROM RankedPrices
WHERE rn = 1

UNION

SELECT 
    product_id, 
    10 AS price
FROM Products
GROUP BY product_id
HAVING MIN(change_date) > '2019-08-16';

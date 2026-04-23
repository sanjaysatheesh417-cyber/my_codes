#https://leetcode.com/problems/product-sales-analysis-iii/?envType=study-plan-v2&envId=top-sql-50

solution:
SELECT
    product_id,
    year AS first_year,
    quantity,
    price
FROM (
    SELECT 
        *,
        RANK() OVER (PARTITION BY product_id ORDER BY year ASC) as rnk
    FROM Sales
) t
WHERE rnk = 1;

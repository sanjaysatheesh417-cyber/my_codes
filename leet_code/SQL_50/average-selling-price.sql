#https://leetcode.com/problems/average-selling-price/?envType=study-plan-v2&envId=top-sql-50

solution:
SELECT 
    P.product_id, 
    CASE
        WHEN ROUND((SUM(units*price)/SUM(units)),2) IS NULL THEN 0.00
        ELSE  ROUND((SUM(units*price)/SUM(units)),2)
    END AS average_price
FROM Prices P
LEFT JOIN UnitsSold U
    ON purchase_date BETWEEN start_date AND end_date AND P.product_id = U.product_id
GROUP BY P.product_id;

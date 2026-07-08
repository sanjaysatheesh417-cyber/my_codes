#https://leetcode.com/problems/group-sold-products-by-the-date/submissions/2060568152/?envType=study-plan-v2&envId=top-sql-50

solution:
SELECT
    sell_date,
    COUNT(DISTINCT product) AS num_sold,
    GROUP_CONCAT(DISTINCT(product) ORDER BY product ASC SEPARATOR ',') AS products
FROM Activities
GROUP BY sell_date
ORDER BY sell_date;

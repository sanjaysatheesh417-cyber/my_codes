#https://leetcode.com/problems/monthly-transactions-i/?envType=study-plan-v2&envId=top-sql-50

solution:
SELECT
    country,
    DATE_FORMAT(trans_date, '%Y-%m') AS month,
    COUNT(amount) AS trans_count,
    SUM(CASE WHEN state = "approved" THEN 1 ELSE 0 END) AS approved_count,
    SUM(amount) AS trans_total_amount,
    SUM(CASE WHEN state = "approved" THEN amount ELSE 0 END) AS approved_total_amount
FROM Transactions
GROUP BY country, month;

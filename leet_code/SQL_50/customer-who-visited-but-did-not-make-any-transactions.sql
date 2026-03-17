#https://leetcode.com/problems/customer-who-visited-but-did-not-make-any-transactions/?envType=study-plan-v2&envId=top-sql-50

solution:
SELECT
    customer_id,
    COUNT(V.visit_id) AS count_no_trans
FROM visits V
LEFT JOIN Transactions T
    ON V.visit_id = T.visit_id
WHERE T.visit_id IS NULL
GROUP BY customer_id
ORDER BY count_no_trans DESC;

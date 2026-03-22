#https://leetcode.com/problems/confirmation-rate/?envType=study-plan-v2&envId=top-sql-50

solution:
SELECT
    S.user_id,
    CASE
        WHEN ROUND((subq.total/COUNT(C.user_id)),2) IS NULL THEN 0.00
        ELSE ROUND((subq.total/COUNT(C.user_id)),2)
    END AS confirmation_rate
FROM Signups S
LEFT JOIN Confirmations C
    ON C.user_id = S.user_id
LEFT JOIN (SELECT user_id, COUNT(action) AS total FROM Confirmations WHERE action = "confirmed" GROUP BY User_id) subq
    ON subq.user_id = C.user_id
GROUP BY S.user_id;

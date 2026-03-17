#https://leetcode.com/problems/rising-temperature/?envType=study-plan-v2&envId=top-sql-50

solution:
SELECT 
    DISTINCT Wt.id
FROM Weather W
JOIN Weather Wt
    ON W.recordDate < Wt.recordDate
WHERE W.temperature < Wt.temperature AND (DATEDIFF(Wt.recordDate,W.recordDate)= 1)
GROUP BY W.id;

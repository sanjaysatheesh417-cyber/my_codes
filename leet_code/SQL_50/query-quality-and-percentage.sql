#https://leetcode.com/problems/queries-quality-and-percentage/?envType=study-plan-v2&envId=top-sql-50

solution:
SELECT
    query_name,
    ROUND(AVG(rating/position),2) AS quality,
    ROUND((SUM(CASE WHEN rating < 3 THEN 1 ELSE 0 END)/COUNT(*))*100,2) AS poor_query_percentage
FROM Queries
GROUP BY query_name;

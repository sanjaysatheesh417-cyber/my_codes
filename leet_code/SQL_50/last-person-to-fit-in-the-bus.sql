#https://leetcode.com/problems/last-person-to-fit-in-the-bus/submissions/2026339223/?envType=study-plan-v2&envId=top-sql-50

solution:
WITH cuml AS (
    SELECT
        turn,
        person_name,
        weight,
        SUM(weight) OVER(ORDER BY turn) AS cum_weight
    FROM Queue
)

SELECT
    person_name
FROM cuml
WHERE cum_weight <= 1000
ORDER BY turn DESC
LIMIT 1;

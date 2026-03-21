#https://leetcode.com/problems/employee-bonus/description/?envType=study-plan-v2&envId=top-sql-50

solution:
SELECT
    name,
    bonus
FROM Employee E
LEFT JOIN Bonus B
    ON E.empId = B.empId
WHERE bonus IS NULL OR bonus < 1000;

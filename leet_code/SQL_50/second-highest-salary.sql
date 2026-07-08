#https://leetcode.com/problems/second-highest-salary/submissions/2060553724/?envType=study-plan-v2&envId=top-sql-50

solution:
SELECT (
    SELECT DISTINCT salary
    FROM Employee
    ORDER BY salary DESC
    LIMIT 1 OFFSET 1
) AS SecondHighestSalary;

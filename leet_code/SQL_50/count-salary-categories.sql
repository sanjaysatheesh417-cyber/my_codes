#https://leetcode.com/problems/count-salary-categories/?envType=study-plan-v2&envId=top-sql-50

solution:
SELECT 
    'Low Salary' AS category, 
    COUNT(*) AS accounts_count 
FROM Accounts 
WHERE income < 20000
UNION ALL
SELECT
    'Average Salary',
    COUNT(*) 
FROM Accounts 
WHERE income BETWEEN 20000 AND 50000
UNION ALL
SELECT
    'High Salary',
    COUNT(*)
FROM Accounts 
WHERE income > 50000;

#https://leetcode.com/problems/replace-employee-id-with-the-unique-identifier/submissions/1950172296/?envType=study-plan-v2&envId=top-sql-50

solution:
SELECT 
    unique_id,
    name
FROM Employees E
LEFT JOIN EmployeeUNI EU
ON E.id = EU.id;

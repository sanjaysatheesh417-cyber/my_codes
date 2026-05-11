#https://leetcode.com/problems/the-number-of-employees-which-report-to-each-employee/submissions/2000669841/?envType=study-plan-v2&envId=top-sql-50

solution:
SELECT
    E.employee_id,
    E.name,
    COUNT(S.employee_id) AS reports_count,
    ROUND(AVG(S.age),0) AS average_age
FROM Employees E
JOIN Employees S
    ON E.employee_id = S.reports_to
GROUP BY E.employee_id
ORDER BY E.employee_id;

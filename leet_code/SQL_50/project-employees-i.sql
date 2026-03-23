#https://leetcode.com/problems/project-employees-i/submissions/1956857225/?envType=study-plan-v2&envId=top-sql-50

solution:
SELECT P.project_id ,ROUND(AVG(E.experience_years),2) AS average_years
FROM Project P
JOIN Employee E
    ON P.employee_id = E.employee_id
GROUP BY P.project_id;

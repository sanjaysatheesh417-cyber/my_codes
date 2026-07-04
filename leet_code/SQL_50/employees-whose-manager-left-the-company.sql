#https://leetcode.com/problems/employees-whose-manager-left-the-company/submissions/2055439019/?envType=study-plan-v2&envId=top-sql-50

SELECT 
    employee_id
FROM Employees
WHERE manager_id IS NOT NULL
  AND manager_id NOT IN (
      SELECT employee_id 
      FROM Employees 
  )
  AND salary < 30000
ORDER BY employee_id;

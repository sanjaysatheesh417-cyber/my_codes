#https://leetcode.com/problems/patients-with-a-condition/submissions/2060515231/?envType=study-plan-v2&envId=top-sql-50

solution:
SELECT
    *
FROM Patients
WHERE conditions LIKE 'DIAB1%' 
   OR conditions LIKE '% DIAB1%';

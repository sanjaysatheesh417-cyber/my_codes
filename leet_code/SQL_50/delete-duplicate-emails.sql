#https://leetcode.com/problems/delete-duplicate-emails/submissions/2060528353/?envType=study-plan-v2&envId=top-sql-50

solution:
WITH rn AS (
    SELECT id,
           ROW_NUMBER() OVER (PARTITION BY email ORDER BY id) as row_num
    FROM Person
)
DELETE FROM Person 
WHERE id IN (SELECT id FROM rn WHERE row_num > 1);

#https://leetcode.com/problems/find-users-with-valid-e-mails/submissions/2061186857/?envType=study-plan-v2&envId=top-sql-50

solution:
SELECT 
    *
FROM Users
WHERE mail REGEXP '^[a-zA-Z][a-zA-Z0-9_.-]*@leetcode\\.com$'
  AND BINARY mail LIKE '%@leetcode.com';

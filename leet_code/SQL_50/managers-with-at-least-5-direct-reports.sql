#https://leetcode.com/problems/managers-with-at-least-5-direct-reports/?source=submission-noac

solution:
SELECT
    name
FROM (SELECT managerId FROM Employee GROUP BY managerId HAVING COUNT(managerId) >= 5) subq
JOIN Employee E
    ON subq.managerId = E.id;

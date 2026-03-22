#https://leetcode.com/problems/not-boring-movies/submissions/1955688069/?envType=study-plan-v2&envId=top-sql-50

solution:
SELECT *
FROM Cinema
WHERE description != "boring" AND id%2 != 0
ORDER BY rating DESC;

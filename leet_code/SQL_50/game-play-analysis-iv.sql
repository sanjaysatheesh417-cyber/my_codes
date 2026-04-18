#https://leetcode.com/problems/game-play-analysis-iv/?envType=study-plan-v2&envId=top-sql-50

solution:
WITH player_log AS (
    SELECT 
        player_id, 
        event_date,
        MIN(event_date) OVER(PARTITION BY player_id) as first_login,
        LEAD(event_date) OVER(PARTITION BY player_id ORDER BY event_date) as next_login
    FROM Activity)
SELECT 
    ROUND(COUNT(DISTINCT CASE WHEN next_login = first_login + INTERVAL 1 DAY THEN player_id END)/COUNT(DISTINCT player_id),2) AS fraction
FROM player_log
WHERE event_date = first_login;

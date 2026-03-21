#https://leetcode.com/problems/average-time-of-process-per-machine/description/?envType=study-plan-v2&envId=top-sql-50

solution:
SELECT
    A.machine_id AS machine_id,
    ROUND(AVG(Ac.timestamp - A.timestamp),3) AS processing_time
FROM Activity A
JOIN Activity Ac
    ON  A.machine_id = Ac.machine_id AND A.process_id = Ac.process_id
WHERE A.activity_type = "start" AND Ac.activity_type = "end"
GROUP BY A.machine_id;

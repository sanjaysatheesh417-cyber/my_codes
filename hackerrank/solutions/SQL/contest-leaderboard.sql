#https://www.hackerrank.com/challenges/contest-leaderboard/problem

solution:
SELECT
    H.hacker_id,
    H.name,
    SUM(MAXIM) AS TOTAL
FROM (SELECT MAX(score) AS MAXIM,hacker_id FROM SUBMISSIONS GROUP BY hacker_id, challenge_id) S
JOIN HACKERS H
    ON S.hacker_id = H.hacker_id
GROUP BY H.hacker_id, H.name
HAVING TOTAL != 0
ORDER BY SUM(MAXIM) DESC , H.hacker_id ASC;

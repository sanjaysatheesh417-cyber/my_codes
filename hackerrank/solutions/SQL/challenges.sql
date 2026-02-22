#https://www.hackerrank.com/challenges/challenges/problem

solution:
SELECT 
    H.hacker_id,
    H.name,
    COUNT(challenge_id) AS NUMBEROFCHALLENGES
FROM HACKERS H
JOIN CHALLENGES C
    ON C.hacker_id = H.hacker_id
GROUP BY H.hacker_id, H.name
HAVING NUMBEROFCHALLENGES NOT IN (SELECT NUM FROM (SELECT COUNT(challenge_id) AS NUM FROM CHALLENGES GROUP BY hacker_id) SUBQ GROUP BY NUM HAVING COUNT(*) > 1) OR NUMBEROFCHALLENGES = (SELECT MAX(NUM) FROM (SELECT COUNT(challenge_id) AS NUM FROM CHALLENGES GROUP BY hacker_id) SUBQ1)
ORDER BY NUMBEROFCHALLENGES DESC, H.hacker_id ASC;

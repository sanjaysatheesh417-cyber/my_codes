#https://www.hackerrank.com/challenges/full-score/problem

solution:
SELECT 
    H.hacker_id,
    H.name
FROM hackers H
JOIN submissions S
    ON H.hacker_id = S.hacker_id
JOIN challenges C
    ON C.challenge_id = S.challenge_id
JOIN difficulty D
    ON D.difficulty_level = C.difficulty_level
WHERE S.score = D.score
GROUP BY H.hacker_id, H.name
HAVING COUNT(S.challenge_id) > 1
ORDER BY COUNT(S.challenge_id) DESC, H.hacker_id ASC;

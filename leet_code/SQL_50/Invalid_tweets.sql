#https://leetcode.com/problems/invalid-tweets/submissions/1950131330/?envType=study-plan-v2&envId=top-sql-50

solution:
SELECT tweet_id
FROM Tweets
WHERE CHAR_LENGTH(content) > 15;

#https://www.hackerrank.com/challenges/revising-aggregations-sum/problem

solution:
SELECT SUM(POPULATION)
FROM CITY
WHERE DISTRICT = "California";

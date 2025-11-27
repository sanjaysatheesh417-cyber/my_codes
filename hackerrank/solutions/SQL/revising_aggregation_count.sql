#https://www.hackerrank.com/challenges/revising-aggregations-the-count-function/problem?isFullScreen=true

solution:
SELECT COUNT(ID)
FROM CITY
WHERE POPULATION > 100000;

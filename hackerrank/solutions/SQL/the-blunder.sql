#https://www.hackerrank.com/challenges/the-blunder/problem

solution:
SELECT CEILING(AVG(SALARY)-AVG(REPLACE(CAST(SALARY AS CHAR),"0",""))) AS DIFFERENCE
FROM EMPLOYEES;

#https://www.hackerrank.com/challenges/japan-population/problem

solution:
SELECT SUM(POPULATION)
FROM CITY
WHERE COUNTRYCODE= "JPN";

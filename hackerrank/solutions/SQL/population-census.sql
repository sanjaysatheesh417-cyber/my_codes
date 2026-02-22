#https://www.hackerrank.com/challenges/asian-population/problem

solution:
SELECT SUM(C.POPULATION) AS TOTALPOP
FROM CITY C
JOIN COUNTRY CO ON C.COUNTRYCODE = CO.CODE
WHERE CO.CONTINENT = "Asia";

#https://www.hackerrank.com/challenges/african-cities/problem

solution:
SELECT C.NAME AS CITIES
FROM CITY C
JOIN COUNTRY CO ON C.COUNTRYCODE = CO.CODE
WHERE CO.CONTINENT = "AFRICA";

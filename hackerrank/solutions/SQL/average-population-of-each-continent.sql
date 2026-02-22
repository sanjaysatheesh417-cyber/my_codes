#https://www.hackerrank.com/challenges/average-population-of-each-continent/problem

solution:
SELECT 
    CO.continent,
    fLOOR(AVG(C.population))
FROM CITY C
JOIN COUNTRY CO ON
    C.countrycode = CO.code
GROUP BY CO.continent;

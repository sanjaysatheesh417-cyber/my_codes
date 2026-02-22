#https://www.hackerrank.com/challenges/weather-observation-station-20/problem

solution:
SELECT ROUND(ST.LAT_N, 4)
FROM (SELECT LAT_N,ROW_NUMBER() OVER (ORDER BY LAT_N) AS RN, COUNT(*) OVER() AS TOTAL FROM STATION) AS ST
WHERE RN = FLOOR(TOTAL/2) + 1;

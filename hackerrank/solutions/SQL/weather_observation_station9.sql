#https://www.hackerrank.com/challenges/weather-observation-station-9/problem?isFullScreen=true

solution:
SELECT DISTINCT CITY
FROM STATION
WHERE NOT (CITY LIKE "A%" OR CITY LIKE "E%" OR CITY LIKE "I%" OR CITY LIKE "O%" OR CITY LIKE "U%");

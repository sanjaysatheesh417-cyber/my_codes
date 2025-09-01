#https://www.hackerrank.com/challenges/weather-observation-station-3/problem?isFullScreen=true

solution:
SELECT DISTINCT CITY FROM STATION WHERE ID%2 = 0;

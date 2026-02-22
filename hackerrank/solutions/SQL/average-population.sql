#https://www.hackerrank.com/challenges/average-population/problem

solution:
SELECT TRUNCATE(AVG(POPULATION),0) as average_population
FROM CITY;

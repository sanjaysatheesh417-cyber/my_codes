#https://www.hackerrank.com/challenges/the-pads/problem

solution:
SELECT RPAD(Name,(LENGTH(Name)+3),CONCAT("(",LEFT(Occupation, 1),")"))
FROM OCCUPATIONS
ORDER BY Name;
SELECT CONCAT("There are a total of ", COUNT(Name)," ",LOWER(Occupation),"s.")
FROM OCCUPATIONS
GROUP BY Occupation
ORDER BY COUNT(Name);

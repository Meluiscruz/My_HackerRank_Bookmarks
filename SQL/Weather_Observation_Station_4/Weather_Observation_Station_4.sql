USE coderunner;
SELECT COUNT(city) - COUNT(DISTINCT city)
FROM station;
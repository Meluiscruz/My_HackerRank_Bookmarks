USE coderunner;
SELECT name
FROM students
WHERE marks>75 ORDER BY SUBSTRING(Name,-3,LENGTH(Name)),ID;
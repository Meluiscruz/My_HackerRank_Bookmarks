SELECT
CASE 
    WHEN A+B>C AND A+C>B AND B+C>A THEN /*The problem was here! Be careful with AND/OR*/
        CASE
            WHEN A=B AND B=C THEN 'Equilateral'
            WHEN A=B OR B=C OR A=C THEN 'Isosceles'
            WHEN A<>B OR B<>C OR A<>C THEN 'Scalene'
        END
    ELSE 'Not A Triangle' 
END AS kind_of_triangles
FROM triangles;
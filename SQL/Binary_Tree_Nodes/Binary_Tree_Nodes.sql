SELECT n,(CASE
                WHEN p is NULL THEN 'Root'
                WHEN n in (SELECT DISTINCT p FROM bst) THEN 'Inner'
                ELSE 'Leaf'
          END) AS Type_of_node
FROM bst
ORDER BY n ASC
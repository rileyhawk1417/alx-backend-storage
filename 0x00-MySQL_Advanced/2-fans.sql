-- Select metal bands with specific query 
SELECT origins, SUM(fans) AS 'nb_fans'
        FROM metal_bands
        GROUP BY origin
        ORDER BY nb_fans DESC;

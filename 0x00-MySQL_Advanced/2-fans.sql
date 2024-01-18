SELECT metal_bands.origins, SUM(fans) AS 'nb_fans' FROM metal_bands GROUP BY metal_bands.origin ORDER BY SUM(metal_bands.fans) DESC LIMIT 9;

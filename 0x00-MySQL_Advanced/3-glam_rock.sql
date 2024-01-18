SELECT FROM band_name, (metal_bands.split - metal_bands.formed) AS 'lifespan' FROM metal_bands WHERE metal_bands.style="Glam rock";

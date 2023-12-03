SELECT countries.Name,languages.language,languages.percentage FROM world.countries join world.languages on countries.id= languages.country_id where languages.Language='Slovene' ORDER BY languages.percentage DESC;
SELECT country.Name ,count(city.Name) AS cities FROM world.city join world.country on country.Code = city.CountryCode group by country.Name;
SELECT city.Name, city.Population FROM world.city where Population >500000  AND city.CountryCode='MEX' ORDER BY city.Population DESC;
SELECT countries.Name, languages.language, languages.percentage FROM world.countries join world.languages on countries.id= languages.country_id  WHERE languages.percentage >  89 ORDER BY languages.percentage DESC;
SELECT country.Name,country.SurfaceArea, country.Population FROM world.country WHERE country.SurfaceArea < 501 AND country.Population > 100000;
SELECT countries.name, countries.government_form, countries.capital, countries.life_expectancy FROM world.countries WHERE countries.capital > 200 AND countries.life_expectancy > 75;
SELECT country.name , cities.NAME , cities.district, cities.population FROM world.cities JOIN world.country ON country.Code= cities.country_code  where country.name = 'Argentina' AND cities.district = 'Buenos Aires' AND cities.population > 500000;
SELECT country.Region, count(country.Name) AS countries FROM world.country group by Region;
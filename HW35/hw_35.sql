-- 1. Лысые злодеи 90-х годов
SELECT name, FIRST_APPEARANCE, appearances
FROM MarvelCharacters
WHERE year BETWEEN 1990 AND 1999 
    AND HAIR = 'bald'
    OR ALIGN = 'Bad Characters'
LIMIT 94;


-- Герои с тайной идентичностью и необычными глазами
SELECT name, FIRST_APPEARANCE, eye
FROM MarvelCharacters
WHERE identify IS NOT NULL
    AND eye NOT IN ('blue', 'brown', 'green')
    AND FIRST_APPEARANCE IS NOT NULL
LIMIT 1027;


-- 3. Персонажи с изменяющимся цветом волос
SELECT name, HAIR
FROM MarvelCharacters
WHERE HAIR = 'Variable Hair';


-- 4. Женские персонажи с редким цветом глаз
SELECT name, eye
FROM MarvelCharacters
WHERE SEX = 'Female Characters' 
    AND (eye = 'Gold Eyes' OR eye = 'Amber Eyes')
ORDER BY eye;
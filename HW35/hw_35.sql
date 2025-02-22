-- 1. Лысые злодеи 90-х годов
SELECT name, Year, appearances
FROM MarvelCharacters
WHERE HAIR = 'Bald' AND ALIGN = 'Bad Characters'
    AND Year BETWEEN 1990 AND 1999;



-- Герои с тайной идентичностью и необычными глазами
SELECT name, FIRST_APPEARANCE, eye
FROM MarvelCharacters
WHERE identify = 'Secret Identity'
    AND eye NOT IN ('Blue Eyes', 'Brown Eyes', 'Green Eyes')
    AND FIRST_APPEARANCE IS NOT NULL;


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


-- 5. Персонажи без двойной идентичности, сортированные по году появления
SELECT name, FIRST_APPEARANCE
FROM MarvelCharacters
WHERE identify = 'No Dual Identity'
ORDER BY Year DESC;
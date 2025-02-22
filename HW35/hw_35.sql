-- 1. Лысые злодеи 90-х годов
SELECT name, FIRST_APPEARANCE, appearances
FROM MarvelCharacters
WHERE year BETWEEN 1990 AND 1999 
    AND HAIR = 'bald'
    OR ALIGN = 'Bad Characters'
LIMIT 94;

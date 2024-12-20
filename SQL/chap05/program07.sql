-- 보호소에서 중성화한 동물
SELECT ao.ANIMAL_ID AS ANIMAL_ID, ao.ANIMAL_TYPE AS ANIMAL_TYPE, ao.NAME AS NAME
FROM animal_ins ai
RIGHT JOIN animal_outs ao ON ai.ANIMAL_ID = ao.ANIMAL_ID
WHERE ai.SEX_UPON_INTAKE LIKE "Intact%" and ao.SEX_UPON_OUTCOME NOT LIKE "Intact%"
ORDER BY ao.ANIMAL_ID;
-- 있었는데요 없었습니다
SELECT ai.ANIMAL_ID AS "ANIMAL_ID", ai.NAME AS "NAME"
FROM animal_ins ai 
LEFT OUTER JOIN animal_outs ao ON ai.ANIMAL_ID = ao.ANIMAL_ID
WHERE ai.DATETIME > ao.DATETIME
ORDER BY ai.DATETIME;
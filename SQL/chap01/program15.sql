-- 상위 n개 레코드
SELECT NAME
FROM animal_ins
WHERE DATETIME = (SELECT MIN(DATETIME) FROM animal_ins);
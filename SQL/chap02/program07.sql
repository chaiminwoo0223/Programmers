-- 중복 제거하기
SELECT COUNT(DISTINCT NAME) AS "count"
FROM animal_ins
WHERE NAME IS NOT NULL;
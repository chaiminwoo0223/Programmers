-- 잔챙이 잡은 수 구하기
SELECT COUNT(*) AS "FISH_COUNT"
FROM fish_info
WHERE LENGTH IS NULL;
-- 잡은 물고기 중 가장 큰 물고기의 길이 구하기
SELECT CONCAT(length, "cm") AS "MAX_LENGTH"
FROM fish_info
ORDER BY length DESC
LIMIT 1;
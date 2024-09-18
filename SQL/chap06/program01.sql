-- 한 해에 잡은 물고기 수 구하기
SELECT COUNT(*) AS "FISH_COUNT"
FROM fish_info
WHERE YEAR(TIME) = 2021;
-- 월별 잡은 물고기 수 구하기
SELECT COUNT(fish_type) AS "FISH_COUNT", MONTH(time) AS "MONTH"
FROM fish_info
GROUP BY MONTH(time)
ORDER BY MONTH(time);
-- 가장 큰 물고기 10마리 구하기
SELECT ID, LENGTH
FROM fish_info
ORDER BY LENGTH DESC, ID
LIMIT 10;
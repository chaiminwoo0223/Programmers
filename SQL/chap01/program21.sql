-- 특정 물고기를 잡은 총 수 구하기
SELECT COUNT(*) AS FISH_COUNT
FROM fish_info fi
INNER JOIN fish_name_info fn ON fi.FISH_TYPE = fn.FISH_TYPE
WHERE FISH_NAME = "BASS" OR FISH_NAME = "SNAPPER";
-- 물고기 종류 별 잡은 수 구하기
SELECT COUNT(fn.FISH_TYPE) AS "FISH_COUNT", fn.FISH_NAME AS "FISH_NAME"
FROM fish_info fi
INNER JOIN fish_name_info fn ON fi.FISH_TYPE = fn.FISH_TYPE
GROUP BY fn.FISH_NAME
ORDER BY COUNT(fn.FISH_TYPE) DESC;
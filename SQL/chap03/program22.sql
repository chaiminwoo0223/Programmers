-- 입양 시각 구하기(2)
WITH RECURSIVE CTE AS (
SELECT 0 AS NUM -- 시작점 설정
UNION ALL
SELECT NUM + 1 -- 반복 설정
FROM CTE
WHERE NUM < 23) -- 종료점 설정

SELECT NUM AS HOUR, COUNT(DATETIME) AS COUNT
FROM ANIMAL_OUTS o
RIGHT JOIN CTE c ON HOUR(o.DATETIME) = c.NUM
GROUP BY HOUR
ORDER BY HOUR;
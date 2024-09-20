-- 노선별 평균 역 사이 거리 조회하기
-- 정렬: 문자열 vs 숫자
SELECT ROUTE, 
       CONCAT(ROUND(SUM(D_BETWEEN_DIST), 1), "km") AS "TOTAL_DISTANCE", 
       CONCAT(ROUND(AVG(D_BETWEEN_DIST), 2), "km") AS "AVERAGE_DISTANCE"
FROM subway_distance
GROUP BY ROUTE
ORDER BY SUM(D_BETWEEN_DIST) DESC;
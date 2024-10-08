-- 즐겨찾기가 가장 많은 식당 정보 출력하기
SELECT f.FOOD_TYPE AS "FOOD_TYPE", f.REST_ID AS "REST_ID", f.REST_NAME AS "REST_NAME", f.FAVORITES AS "FAVORITES"
FROM rest_info f
INNER JOIN (SELECT FOOD_TYPE, MAX(FAVORITES) AS "FAVORITES" FROM rest_info GROUP BY FOOD_TYPE) t ON f.FAVORITES = t.FAVORITES AND f.FOOD_TYPE = t.FOOD_TYPE
ORDER BY FOOD_TYPE DESC;
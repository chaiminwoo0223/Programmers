-- 식품분류별 가장 비싼 식품의 정보 조회하기
SELECT CATEGORY, PRICE AS MAX_PRICE, PRODUCT_NAME
FROM food_product
WHERE CATEGORY IN ("과자", "국", "김치", "식용유") AND 
      PRICE IN (SELECT MAX(PRICE) FROM food_product WHERE CATEGORY IN ("과자", "국", "김치", "식용유") GROUP BY CATEGORY)
ORDER BY MAX_PRICE DESC;
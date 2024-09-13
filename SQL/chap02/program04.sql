-- 가격이 제일 비싼 식품의 정보 출력하기
SELECT *
FROM food_product
WHERE PRICE = (SELECT MAX(PRICE) FROM food_product); -- 서브쿼리
-- 조건별로 분류하여 주문상태 출력하기
SELECT ORDER_ID, PRODUCT_ID, OUT_DATE,
       IF(DATE_FORMAT(OUT_DATE, "%Y-%m-%d") <= "2022-05-01", "출고완료",
          IF(DATE_FORMAT(OUT_DATE, "%Y-%m-%d") > "2022-05-01", "출고대기", "출고미정")) AS "출고여부"
FROM food_order;
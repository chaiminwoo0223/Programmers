-- 상품 별 오프라인 매출 구하기
SELECT p.PRODUCT_CODE AS "PRODUCT_CODE", SUM(p.PRICE * os.SALES_AMOUNT) AS "SALES"
FROM product p
INNER JOIN offline_sale os ON p.PRODUCT_ID = os.PRODUCT_ID
GROUP BY PRODUCT_CODE
ORDER BY SALES DESC, PRODUCT_CODE;
-- 성분으로 구분한 아이스크림 총 주문량
SELECT ii.INGREDIENT_TYPE, SUM(fh.TOTAL_ORDER) AS "TOTAL_ORDER"
FROM first_half fh
INNER JOIN icecream_info ii ON fh.FLAVOR = ii.FLAVOR
GROUP BY ii.INGREDIENT_TYPE
ORDER BY TOTAL_ORDER;
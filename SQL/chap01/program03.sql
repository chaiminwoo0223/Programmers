-- 과일로 만든 아이스크림 고르기
SELECT fh.flavor AS "FLAVOR"
FROM first_half fh
INNER JOIN icecream_info ii ON fh.flavor = ii.flavor
WHERE total_order > 3000 and ingredient_type = "fruit_based"
ORDER BY total_order DESC;
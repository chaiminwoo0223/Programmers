-- 업그레이드 할 수 없는 아이템 구하기
SELECT ii.ITEM_ID, ii.ITEM_NAME, ii.RARITY
FROM item_info ii 
LEFT OUTER JOIN item_tree it ON ii.ITEM_ID = it.PARENT_ITEM_ID
WHERE it.PARENT_ITEM_ID IS NULL
ORDER BY ii.ITEM_ID DESC;
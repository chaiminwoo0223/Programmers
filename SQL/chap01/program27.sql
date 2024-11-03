-- 대장균들의 자식의 수 구하기
SELECT e.ID AS ID, (SELECT COUNT(*) FROM ecoli_data WHERE PARENT_ID = e.ID) AS CHILD_COUNT
FROM ecoli_data e
ORDER BY ID;
-- 특정 세대의 대장균 찾기
SELECT ID
FROM ecoli_data
WHERE PARENT_ID IN (SELECT ID 
                    FROM ecoli_data 
                    WHERE PARENT_ID IN (SELECT ID
                                        FROM ecoli_data 
                                        WHERE PARENT_ID IS NULL))
ORDER BY ID
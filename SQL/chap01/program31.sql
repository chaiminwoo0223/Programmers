-- 부모의 형질을 모두 가지는 대장균 찾기
SELECT a.ID AS ID, a.GENOTYPE AS GENOTYPE, b.GENOTYPE AS PARENT_GENOTYPE
FROM ecoli_data a
INNER JOIN ecoli_data b ON a.PARENT_ID = b.ID 
WHERE a.GENOTYPE & b.GENOTYPE = b.GENOTYPE
ORDER BY ID;
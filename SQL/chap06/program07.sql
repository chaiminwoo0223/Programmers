-- 이름에 el이 들어가는 동물 찾기
SELECT ANIMAL_ID, NAME 
FROM animal_ins
WHERE ANIMAL_TYPE = "Dog" AND NAME LIKE "%el%"
ORDER BY NAME;
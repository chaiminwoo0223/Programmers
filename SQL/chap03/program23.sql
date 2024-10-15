-- 연간 평가점수에 해당하는 평가 등급 및 성과금 조회하기
SELECT EMP_NO, EMP_NAME, GRADE, IF(GRADE = 'S', SAL * 0.2, IF(GRADE = 'A', SAL * 0.15, IF(GRADE = 'B', SAL * 0.1, 0))) AS BONUS
FROM (SELECT he.EMP_NO AS EMP_NO, EMP_NAME, SAL, IF(AVG(SCORE) >= 96, 'S', IF(AVG(SCORE) >= 90, 'A', IF(AVG(SCORE) >= 80, 'B', 'C'))) AS GRADE
      FROM hr_employees he
      INNER JOIN hr_grade hg ON he.EMP_NO = hg.EMP_NO
      LEFT JOIN hr_department hd ON he.DEPT_ID = hd.DEPT_ID
      GROUP BY EMP_NO
      ORDER BY EMP_NO) t
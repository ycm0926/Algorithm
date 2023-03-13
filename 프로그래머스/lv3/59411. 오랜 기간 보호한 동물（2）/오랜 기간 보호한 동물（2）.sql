SELECT A.ANIMAL_ID, A.NAME
FROM ANIMAL_INS A JOIN ANIMAL_OUTS B
ON A.ANIMAL_ID = B.ANIMAL_ID
WHERE DATEDIFF(B.DATETIME, A.DATETIME)
ORDER BY DATEDIFF(B.DATETIME, A.DATETIME) DESC
LIMIT 2
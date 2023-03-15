SELECT A.MEMBER_NAME, B.REVIEW_TEXT, DATE_FORMAT(B.REVIEW_DATE, '%Y-%m-%d') AS REVIEW_DATE
FROM MEMBER_PROFILE A JOIN REST_REVIEW B
ON A.MEMBER_ID = B.MEMBER_ID
WHERE A.MEMBER_ID IN (SELECT MEMBER_ID
                        FROM REST_REVIEW
                        GROUP BY MEMBER_ID
                        HAVING count(member_id) = (SELECT COUNT(REVIEW_TEXT) AS 'NUM'
                                FROM REST_REVIEW
                                GROUP BY MEMBER_ID
                                ORDER BY NUM DESC
                                LIMIT 1))
ORDER BY B.REVIEW_DATE, B.REVIEW_TEXT
SELECT NAME, DATETIME
FROM (SELECT NAME, DATETIME
      FROM ANIMAL_INS 
      WHERE ANIMAL_ID NOT IN (SELECT O.ANIMAL_ID
                              FROM ANIMAL_INS I, ANIMAL_OUTS O
                              WHERE I.ANIMAL_ID = O.ANIMAL_ID)
                              ORDER BY datetime ASC)
WHERE ROWNUM <= 3
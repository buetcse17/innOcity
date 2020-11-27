ALTER TABLE CUSTOMER 
ADD PHONE_NUM VARCHAR(50);

UPDATE CUSTOMER C 
SET C.PHONE_NUM = (SELECT PHONE_NUM FROM CUSTOMER_PHONE CP WHERE CP.CUSTOMERID = C.CUSTOMERID);

DROP TABLE CUSTOMER_PHONE;